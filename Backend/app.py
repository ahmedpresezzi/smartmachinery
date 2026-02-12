import discord
from discord.ext import commands
import json
import os
from datetime import datetime
from aiohttp import web
import asyncio
import aiohttp

import os
from dotenv import load_dotenv

# Carica variabili d'ambiente
load_dotenv()

# --- CONFIGURAZIONE ---
TOKEN = os.getenv('DISCORD_TOKEN')
WEBHOOK_LOGS = os.getenv('WEBHOOK_LOGS')
WEBHOOK_PERMS = os.getenv('WEBHOOK_PERMS')

# Memoria per richieste permessi temporanee
# { username: { status: 'pending'|'accepted'|'rejected', role: 'admin', expires: timestamp } }
PERMISSION_REQUESTS = {}

# Risoluzione percorsi assoluta
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if not BASE_DIR: BASE_DIR = os.getcwd()

DB_FILE = os.path.join(BASE_DIR, 'user.json') 
AUDIT_FILE = os.path.join(BASE_DIR, 'audit.json')
ASSETS_FILE = os.path.join(BASE_DIR, 'assets.json')
STATE_FILE = os.path.join(BASE_DIR, 'bot_state.json')
ROOT_DIR = os.path.dirname(BASE_DIR)
FRONTEND_DIR = ROOT_DIR # Frontend files are now in the root

# OpenRouter Config
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
OPENROUTER_MODEL = 'openai/gpt-4o-mini'
OPENROUTER_URL = 'https://openrouter.ai/api/v1/chat/completions'

SYSTEM_CONTEXT = """
Sei l'assistente virtuale ufficiale del software "Smart Machinery Lab".
Il tuo obiettivo è AIUTARE gli utenti con domande ESCLUSIVAMENTE riguardanti il sito e il software Smart Machinery Lab.

REGOLE STRETTE DI COMPORTAMENTO:
1. Rispondi SOLO a domande inerenti a:
   - Gestione Asset (creazione macchine, stati 'Pending' e 'Licensed').
   - Configurazione PLC (Siemens, Rockwell, indirizzi IP, frequenze di campionamento).
   - Validazione Dati / Funzione SCAN (verifica Excel, colonne TAG ID, IT, EN).
   - File Manager (modifica file JSON/Python nelle cartelle 'bsw' o 'webapp').
   - Storage (upload e modifica file .xlsx nel browser).
   - Pannello Admin (gestione licenze utenti, ruoli, audit log).
   - Navigazione generale della Dashboard.

2. SE L'UTENTE FA UNA DOMANDA NON INERENTE (es: meteo, ricette, cultura generale, programmazione generica non legata al software, aiuto per altri siti, ecc.), DEVI DECLINARE CORTESEMENTE:
   "Mi dispiace, ma come assistente dedicato di Smart Machinery Lab posso rispondere solo a domande inerenti alla gestione degli asset, configurazione PLC e funzionalità tecniche di questa piattaforma."

3. Sii professionale, tecnico ma conciso. Usa l'italiano come lingua principale (o segui la lingua dell'utente se inerente al software).

DOCUMENTAZIONE DI RIFERIMENTO RAPIDA:
- Assets: I nuovi asset sono 'Pending'. Diventano 'Licensed' dopo aver salvato la configurazione PLC.
- PLC: Supporto per Siemens e Rockwell. Parametri necessari: IP e frequenze (es. 20ms, 50ms).
- Scan: Pulsante "battito cardiaco" sulla card. Verifica se l'Excel ha le colonne TAG ID, IT, EN.
- File Manager: Icona cartella. Permette l'editing diretto dei file di configurazione generati.
- Storage: Tab per caricare .xlsx e vederli in una tabella editabile.
"""

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# --- ASSETS PERSISTENCE ---
def load_assets():
    if not os.path.exists(ASSETS_FILE): return []
    with open(ASSETS_FILE, 'r', encoding='utf-8') as f:
        try: return json.load(f)
        except: return []

def save_assets(data):
    try:
        with open(ASSETS_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            f.flush()
            os.fsync(f.fileno())
    except Exception as e: print(f"ERR ASSETS: {e}")

# --- UTILITIES ---
def load_db():
    if not os.path.exists(DB_FILE):
        print(f"⚠️ DB Not Found: {DB_FILE}")
        return []
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            # print(f"DEBUG: Loaded {len(data)} users from {DB_FILE}")
            return data
        except Exception as e:
            print(f"❌ Error loading DB: {e}")
            return []

def save_db(data):
    try:
        with open(DB_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            f.flush()
            os.fsync(f.fileno())
    except Exception as e: print(f"ERR DB: {e}")

async def log_event(event_type, message):
    logs = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if os.path.exists(AUDIT_FILE):
        with open(AUDIT_FILE, 'r', encoding='utf-8') as f:
            try: logs = json.load(f)
            except: pass
    logs.append({"timestamp": timestamp, "type": event_type, "message": message})
    with open(AUDIT_FILE, 'w', encoding='utf-8') as f: json.dump(logs[-100:], f, indent=4)
    
    # Invia a Discord
    colors = {"success": 0x2ecc71, "warning": 0xf1c40f, "danger": 0xe74c3c, "info": 0x3498db}
    color = colors.get(event_type, 0x95a5a6)
    
    embed = {
        "title": f"📜 Evento: {event_type.upper()}",
        "description": message,
        "color": color,
        "timestamp": datetime.utcnow().isoformat(),
        "footer": {"text": "Smart Machinery Lab - Audit System"}
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            await session.post(WEBHOOK_LOGS, json={"embeds": [embed]})
    except Exception as e:
        print(f"ERR WEBHOOK: {e}")

def load_state():
    if not os.path.exists(STATE_FILE): return {}
    with open(STATE_FILE, 'r') as f: return json.load(f)

def save_state(state):
    with open(STATE_FILE, 'w') as f: json.dump(state, f, indent=4)

@web.middleware
async def cors_middleware(request, handler):
    # Handle preflight OPTIONS requests
    if request.method == 'OPTIONS':
        return web.Response(status=204, headers={
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            'Access-Control-Max-Age': '86400',
        })
    
    # Handle the actual request
    try:
        response = await handler(request)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        return response
    except web.HTTPException as ex:
        ex.headers['Access-Control-Allow-Origin'] = '*'
        raise ex
    except Exception as e:
        print(f"Middleware Error: {e}")
        raise

async def handle_get_assets(request):
    return web.json_response(load_assets())

async def handle_save_assets(request):
    try:
        data = await request.json()
        save_assets(data)
        return web.json_response({'success': True})
    except Exception as e:
        return web.json_response({'success': False, 'message': str(e)}, status=500)

async def handle_index(request):
    p = os.path.join(FRONTEND_DIR, 'index.html')
    return web.FileResponse(p) if os.path.exists(p) else web.Response(text="index.html not found", status=404)

async def handle_login(request):
    try:
        data = await request.json()
        u, p = data.get('username'), data.get('password')
        db = load_db()
        user = next((x for x in db if x['username'] == u and x['password'] == p), None)
        if user:
            if user['status'] == 'active':
                # Parse User Agent
                ua_string = request.headers.get('User-Agent', '')
                
                os_info = "OS Sconosciuto"
                if "Windows NT 10.0" in ua_string: os_info = "Windows 10/11"
                elif "Windows NT 6.3" in ua_string: os_info = "Windows 8.1"
                elif "Windows NT 6.2" in ua_string: os_info = "Windows 8"
                elif "Windows NT 6.1" in ua_string: os_info = "Windows 7"
                elif "Mac" in ua_string: os_info = "MacOS"
                elif "Linux" in ua_string: os_info = "Linux"

                browser_info = "Browser Sconosciuto"
                if "Edg" in ua_string: browser_info = "Edge"
                elif "Chrome" in ua_string: browser_info = "Chrome"
                elif "Firefox" in ua_string: browser_info = "Firefox"
                elif "Safari" in ua_string: browser_info = "Safari"

                await log_event("info", f"Login effettuato: {u} | {browser_info} - {os_info}")
                return web.json_response({'success': True, 'role': user['role']})
            return web.json_response({'success': False, 'message': 'Account sospeso'})
        return web.json_response({'success': False, 'message': 'Credenziali errate'})
    except: return web.json_response({'success': False}, status=500)

async def handle_get_logs(request):
    logs = []
    if os.path.exists(AUDIT_FILE):
        with open(AUDIT_FILE, 'r') as f: logs = json.load(f)
    return web.json_response(logs)

async def handle_chat(request):
    try:
        data = await request.json()
        msg, hist, lang = data.get('message'), data.get('history', []), data.get('language', 'it')
        messages = [{"role": "system", "content": SYSTEM_CONTEXT}]
        for m in hist[-6:]: messages.append({"role": "user" if m.get('role')=='user' else "assistant", "content": m.get('text','')})
        messages.append({"role": "user", "content": msg})
        async with aiohttp.ClientSession() as session:
            async with session.post(OPENROUTER_URL, headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}"}, json={"model": OPENROUTER_MODEL, "messages": messages}) as resp:
                res = await resp.json()
                return web.json_response({"reply": res['choices'][0]['message']['content']})
    except Exception as e: return web.json_response({"error": str(e)}, status=500)

async def handle_request_perms(request):
    try:
        data = await request.json()
        u = data.get('username')
        duration = data.get('duration') # "5m", "30m", "12h", "1d"
        reason = data.get('reason')
        
        PERMISSION_REQUESTS[u] = {'status': 'pending', 'duration': duration, 'reason': reason}
        
        # Invia al Webhook di Discord
        embed = {
            "title": "⚠️ Richiesta Permessi Admin Temporanei",
            "color": 0xFFA500,
            "fields": [
                {"name": "Utente", "value": f"`{u}`", "inline": True},
                {"name": "Durata", "value": f"`{duration}`", "inline": True},
                {"name": "Motivazione", "value": reason, "inline": False}
            ],
            "footer": {"text": "Usa il pannello bot per approvare/rifiutare"}
        }
        
        async with aiohttp.ClientSession() as session:
            await session.post(WEBHOOK_PERMS, json={"embeds": [embed]})
            
        return web.json_response({'success': True})
    except Exception as e:
        return web.json_response({'success': False, 'message': str(e)}, status=500)

async def handle_check_status(request):
    u = request.query.get('username')
    if not u or u not in PERMISSION_REQUESTS:
        return web.json_response({'status': 'none'})
    
    status_data = PERMISSION_REQUESTS[u]
    # Se accettato, controlla scadenza
    if status_data['status'] == 'accepted':
        if datetime.now().timestamp() > status_data.get('expires', 0):
            status_data['status'] = 'expired'
            PERMISSION_REQUESTS.pop(u, None)
            return web.json_response({'status': 'expired'})
            
    return web.json_response(status_data)

async def handle_admin_get_requests(request):
    # Ritorna tutte le richieste in sospeso o processate
    return web.json_response(PERMISSION_REQUESTS)

async def handle_admin_handle_request(request):
    try:
        data = await request.json()
        u = data.get('username')
        action = data.get('action') # 'approve' or 'reject'
        
        if not u or u not in PERMISSION_REQUESTS:
            return web.json_response({'success': False, 'message': 'Richiesta non trovata'})
            
        req = PERMISSION_REQUESTS[u]
        
        if action == 'approve':
            seconds = 0
            if "5m" in req['duration']: seconds = 5 * 60
            elif "30m" in req['duration']: seconds = 30 * 60
            elif "12h" in req['duration']: seconds = 12 * 3600
            elif "1d" in req['duration']: seconds = 24 * 3600
            
            expires = datetime.now().timestamp() + seconds
            PERMISSION_REQUESTS[u] = {
                'status': 'accepted', 
                'role': 'admin', 
                'expires': expires,
                'duration': req['duration']
            }
            await log_event("success", f"Admin WEB: Permessi ({req['duration']}) concessi a {u}")
            
        elif action == 'reject':
            PERMISSION_REQUESTS[u] = {'status': 'rejected'}
            await log_event("warning", f"Admin WEB: Richiesta di {u} rifiutata")
            
        return web.json_response({'success': True})
    except Exception as e:
        return web.json_response({'success': False, 'message': str(e)}, status=500)

async def handle_admin_create_user(request):
    try:
        data = await request.json()
        u = data.get('username')
        p = data.get('password')
        role = data.get('role', 'user')
        
        if not u or not p: return web.json_response({'success': False, 'message': 'Dati mancanti'})
        
        db = load_db()
        if any(x['username'] == u for x in db):
             return web.json_response({'success': False, 'message': 'Utente esistente'})
             
        db.append({
            "username": u,
            "password": p,
            "role": role,
            "status": "active",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        save_db(db)
        await log_event("success", f"Admin WEB: Creata licenza per {u} ({role})")
        return web.json_response({'success': True})
    except Exception as e:
        return web.json_response({'success': False, 'message': str(e)}, status=500)

async def handle_admin_get_users(request):
    try:
        db = load_db()
        # Return users without passwords for security
        users = []
        now_ts = datetime.now().timestamp()
        
        for u in db:
            user_safe = {k: v for k, v in u.items() if k != 'password'}
            
            # Check for temporary admin permissions
            username = u.get('username')
            if username in PERMISSION_REQUESTS:
                req = PERMISSION_REQUESTS[username]
                if req.get('status') == 'accepted':
                    expires = req.get('expires', 0)
                    if now_ts < expires:
                        user_safe['role'] = 'temp_admin'
                        user_safe['temp_duration'] = req.get('duration')
            
            users.append(user_safe)
            
        return web.json_response(users)
    except Exception as e:
        return web.json_response({'success': False, 'message': str(e)}, status=500)

async def handle_admin_update_user(request):
    try:
        data = await request.json()
        u_target = data.get('username')
        new_role = data.get('role')
        new_status = data.get('status')
        
        if not u_target: return web.json_response({'success': False, 'message': 'Username mancante'})

        db = load_db()
        found = False
        for user in db:
            if user['username'] == u_target:
                if new_role: user['role'] = new_role
                if new_status: user['status'] = new_status
                found = True
                break
        
        if found:
            save_db(db)
            await log_event("info", f"Admin WEB: Aggiornato utente {u_target} (Role: {new_role}, Status: {new_status})")
            return web.json_response({'success': True})
        else:
            return web.json_response({'success': False, 'message': 'Utente non trovato'})
    except Exception as e:
        return web.json_response({'success': False, 'message': str(e)}, status=500)

async def handle_admin_delete_user(request):
    try:
        data = await request.json()
        u_target = data.get('username')
        
        if not u_target: return web.json_response({'success': False, 'message': 'Username mancante'})

        db = load_db()
        initial_len = len(db)
        db = [x for x in db if x['username'] != u_target]
        
        if len(db) < initial_len:
            save_db(db)
            await log_event("warning", f"Admin WEB: Eliminato utente {u_target}")
            return web.json_response({'success': True})
        else:
            return web.json_response({'success': False, 'message': 'Utente non trovato'})
    except Exception as e:
        return web.json_response({'success': False, 'message': str(e)}, status=500)

@web.middleware
async def logger_middleware(request, handler):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {request.method} {request.path}")
    return await handler(request)

async def start_webserver():
    app = web.Application(middlewares=[logger_middleware, cors_middleware])
    app.router.add_post('/login', handle_login)
    app.router.add_get('/logs', handle_get_logs)
    app.router.add_post('/api/chat', handle_chat)
    app.router.add_get('/api/get-assets', handle_get_assets)
    app.router.add_post('/api/save-assets', handle_save_assets)

    app.router.add_post('/api/request-perms', handle_request_perms)
    app.router.add_get('/api/check-status', handle_check_status)
    app.router.add_get('/api/admin/requests', handle_admin_get_requests)
    app.router.add_post('/api/admin/handle-request', handle_admin_handle_request)
    app.router.add_post('/api/admin/create-user', handle_admin_create_user)
    app.router.add_get('/api/admin/users', handle_admin_get_users)
    app.router.add_post('/api/admin/update-user', handle_admin_update_user)
    app.router.add_post('/api/admin/delete-user', handle_admin_delete_user)
    app.router.add_get('/', handle_index)
    if os.path.exists(FRONTEND_DIR): app.router.add_static('/', path=FRONTEND_DIR, name='static')
    LOGOS_DIR = os.path.join(ROOT_DIR, 'logos')
    if os.path.exists(LOGOS_DIR): app.router.add_static('/logos/', path=LOGOS_DIR, name='logos')
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv('PORT', 5001))
    await web.TCPSite(runner, '0.0.0.0', port).start()
    print(f"🚀 SERVER WEB ATTIVO: http://localhost:{port}")

# --- DISCORD COMPONENTS ---

class AdminRequestView(discord.ui.View):
    def __init__(self, username, duration):
        super().__init__(timeout=None)
        self.username = username
        self.duration = duration

    @discord.ui.button(label="Accetta ✅", style=discord.ButtonStyle.success)
    async def approve(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Calcola scadenza
        seconds = 0
        if "5m" in self.duration: seconds = 5 * 60
        elif "30m" in self.duration: seconds = 30 * 60
        elif "12h" in self.duration: seconds = 12 * 3600
        elif "1d" in self.duration: seconds = 24 * 3600
        
        expires = datetime.now().timestamp() + seconds
        PERMISSION_REQUESTS[self.username] = {
            'status': 'accepted', 
            'role': 'admin', 
            'expires': expires,
            'duration': self.duration
        }
        
        await log_event("success", f"Permessi temporanei ({self.duration}) concessi a {self.username}")
        await interaction.response.edit_message(content=f"✅ Permessi concessi a `{self.username}` per {self.duration}.", embed=None, view=None)

    @discord.ui.button(label="Rifiuta ❌", style=discord.ButtonStyle.danger)
    async def reject(self, interaction: discord.Interaction, button: discord.ui.Button):
        PERMISSION_REQUESTS[self.username] = {'status': 'rejected'}
        await interaction.response.edit_message(content=f"❌ Richiesta di `{self.username}` rifiutata.", embed=None, view=None)

# Modal per Modifica Campi (User, Pass)
class EditFieldModal(discord.ui.Modal):
    def __init__(self, title, field_label, user_target, is_pass=False):
        super().__init__(title=title)
        self.user_target = user_target
        self.is_pass = is_pass
        self.field_input = discord.ui.TextInput(label=field_label, default=user_target['password' if is_pass else 'username'], min_length=1, max_length=20)
        self.add_item(self.field_input)

    async def on_submit(self, interaction: discord.Interaction):
        db = load_db()
        new_val = self.field_input.value
        for u in db:
            if u['username'] == self.user_target['username']:
                if self.is_pass:
                    u['password'] = new_val
                    await log_event("info", f"Password cambiata per {u['username']}")
                else:
                    old_name = u['username']
                    u['username'] = new_val
                    await log_event("info", f"Username cambiato: {old_name} -> {new_val}")
                break
        save_db(db)
        await interaction.response.send_message("✅ Modifica salvata con successo!", ephemeral=True)
        # Update original dashboard
        await update_main_dashboard()

# Modal per Registrazione
class RegisterModal(discord.ui.Modal, title="✨ Nuova Licenza"):
    u_in = discord.ui.TextInput(label="Username", placeholder="Inserisci...", min_length=3)
    p_in = discord.ui.TextInput(label="Password", placeholder="Inserisci...", min_length=3)
    async def on_submit(self, interaction: discord.Interaction):
        db = load_db()
        if any(u['username'] == self.u_in.value for u in db):
            return await interaction.response.send_message("❌ Esiste già!", ephemeral=True)
        db.append({"username": self.u_in.value, "password": self.p_in.value, "role": "user", "status": "active", "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        save_db(db)
        await log_event("success", f"Creata licenza: {self.u_in.value}")
        await interaction.response.send_message(f"✅ Creato: {self.u_in.value}", ephemeral=True)
        await update_main_dashboard()

# View di Gestione Singolo Utente
class ManageUserView(discord.ui.View):
    def __init__(self, username):
        super().__init__(timeout=None)
        self.username = username

    @discord.ui.button(label="Cambiata Pwd", style=discord.ButtonStyle.secondary, emoji="🔑")
    async def edit_pwd(self, interaction, btn):
        db = load_db()
        u = next((x for x in db if x['username'] == self.username), None)
        if u: await interaction.response.send_modal(EditFieldModal(f"Edit Pass: {self.username}", "Nuova Password", u, True))

    @discord.ui.button(label="Cambia User", style=discord.ButtonStyle.secondary, emoji="👤")
    async def edit_user(self, interaction, btn):
        db = load_db()
        u = next((x for x in db if x['username'] == self.username), None)
        if u: await interaction.response.send_modal(EditFieldModal(f"Edit User: {self.username}", "Nuovo Username", u, False))

    @discord.ui.button(label="Admin/User", style=discord.ButtonStyle.primary, emoji="🛡️")
    async def toggle_role(self, interaction, btn):
        db = load_db()
        for u in db:
            if u['username'] == self.username:
                u['role'] = 'admin' if u['role'] == 'user' else 'user'
                save_db(db)
                break
        await interaction.response.send_message(f"✅ Ruolo aggiornato per {self.username}", ephemeral=True)
        await update_main_dashboard()

    @discord.ui.button(label="Sospendi/Attiva", style=discord.ButtonStyle.primary, emoji="⛔")
    async def toggle_status(self, interaction, btn):
        db = load_db()
        for u in db:
            if u['username'] == self.username:
                u['status'] = 'suspended' if u['status'] == 'active' else 'active'
                save_db(db)
                break
        await interaction.response.send_message(f"✅ Stato aggiornato per {self.username}", ephemeral=True)
        await update_main_dashboard()

    @discord.ui.button(label="Elimina", style=discord.ButtonStyle.danger, emoji="🗑️")
    async def delete_u(self, interaction, btn):
        db = load_db()
        db = [x for x in db if x['username'] != self.username]
        save_db(db)
        await log_event("warning", f"Licenza eliminata: {self.username}")
        await interaction.response.send_message(f"🗑️ Eliminato: {self.username}", ephemeral=True)
        await update_main_dashboard()

# Menu a tendina per selezione utente
class UserSelect(discord.ui.Select):
    def __init__(self, users):
        options = [discord.SelectOption(label=u['username'], description=f"[{u['role']}] - {u['status']}", emoji="👤") for u in users[-25:]]
        super().__init__(placeholder="Seleziona un utente da gestire...", options=options)
    async def callback(self, interaction):
        username = self.values[0]
        db = load_db()
        u = next((x for x in db if x['username'] == username), None)
        if u:
            emb = discord.Embed(title=f"🛠️ Gestione: {username}", color=0x3498db)
            emb.add_field(name="Username", value=f"`{u['username']}`", inline=True)
            emb.add_field(name="Password", value=f"||{u['password']}||", inline=True)
            emb.add_field(name="Grado", value=f"`{u['role'].upper()}`", inline=True)
            emb.add_field(name="Stato", value="🟢 ATTIVO" if u['status']=='active' else "🔴 SOSPESO", inline=True)
            emb.set_footer(text=f"Creato il: {u['created_at']}")
            await interaction.response.send_message(embed=emb, view=ManageUserView(username), ephemeral=True)

# View Principale Dashboard
class MainAuthView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        db = load_db()
        if db: self.add_item(UserSelect(db))

    @discord.ui.button(label="Nuova Licenza", style=discord.ButtonStyle.success, emoji="➕", custom_id="btn_create")
    async def create_btn(self, interaction, button):
        await interaction.response.send_modal(RegisterModal())

    @discord.ui.button(label="Aggiorna", style=discord.ButtonStyle.secondary, emoji="🔄", custom_id="btn_refresh")
    async def refresh_btn(self, interaction, button):
        await update_main_dashboard()
        try: await interaction.response.send_message("🔄 Dashboard aggiornata!", ephemeral=True)
        except: pass

def create_main_embed():
    db = load_db()
    emb = discord.Embed(title="🔐 Smart Machinery Lab - Central Hub", description="Pannello centralizzato per la gestione delle licenze e del sistema.", color=0xd11617)
    emb.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/3064/3064155.png")
    
    admins = len([u for u in db if u['role'] == 'admin'])
    users = len([u for u in db if u['role'] == 'user'])
    suspended = len([u for u in db if u['status'] != 'active'])

    emb.add_field(name="📊 Statistiche", value=f"👥 Totali: `{len(db)}` | 🛡️ Admin: `{admins}` | 👤 User: `{users}`\n🚫 Sospesi: `{suspended}`", inline=False)
    
    recent_logs = []
    if os.path.exists(AUDIT_FILE):
        with open(AUDIT_FILE, 'r') as f:
            logs = json.load(f)[-3:]
            recent_logs = [f"• [{l['timestamp'][11:]}] {l['message']}" for l in logs]
    
    emb.add_field(name="📜 Ultimi Eventi", value="\n".join(recent_logs) if recent_logs else "Nessun evento recente", inline=False)
    emb.set_footer(text="Smart Machinery Lab v2.0 • Sistema Operativo", icon_url="https://cdn-icons-png.flaticon.com/512/1000/1000997.png")
    return emb

async def update_main_dashboard():
    state = load_state()
    if not state.get('channel_id') or not state.get('message_id'): return
    try:
        channel = bot.get_channel(state['channel_id'])
        if not channel: channel = await bot.fetch_channel(state['channel_id'])
        msg = await channel.fetch_message(state['message_id'])
        await msg.edit(embed=create_main_embed(), view=MainAuthView())
    except Exception as e: print(f"Update GUI Error: {e}")

@bot.event
async def on_message(message):
    if message.webhook_id and message.embeds:
        emb = message.embeds[0]
        if "Richiesta Permessi" in (emb.title or ""):
            u = emb.fields[0].value.replace("`", "")
            d = emb.fields[1].value.replace("`", "")
            await message.channel.send(content=f"🔔 **Nuova Richiesta** di `{u}` (Durata: `{d}`):", view=AdminRequestView(u, d))
    await bot.process_commands(message)

@bot.event
async def on_ready():
    print(f"✅ Bot Discord Online: {bot.user}")
    await asyncio.sleep(2) # Wait for network
    await update_main_dashboard()

@bot.command()
async def auth(ctx):
    # Elimina comando per pulizia
    try: await ctx.message.delete()
    except: pass
    
    msg = await ctx.send(embed=create_main_embed(), view=MainAuthView())
    save_state({'channel_id': ctx.channel.id, 'message_id': msg.id})
    await ctx.send("✅ Hub di gestione attivato. Verrà aggiornato automaticamente ad ogni avvio.", delete_after=5)

@bot.command()
async def prova(ctx): await ctx.send('ciao')

async def main():
    async with bot:
        await start_webserver()
        await bot.start(TOKEN)

if __name__ == "__main__":
    try: asyncio.run(main())
    except KeyboardInterrupt: pass
