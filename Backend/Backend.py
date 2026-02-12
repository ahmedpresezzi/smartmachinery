from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os

# Define the absolute path to the Frontend directory
base_dir = os.path.abspath(os.path.dirname(__file__))
frontend_dir = os.path.join(base_dir, '..', 'Frontend')

app = Flask(__name__, static_folder=frontend_dir)
# Enable CORS so the static frontend can call this API
CORS(app)

from dotenv import load_dotenv

# Carica variabili d'ambiente
load_dotenv()

# Configuration
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
OPENROUTER_MODEL = 'openai/gpt-4o-mini'
OPENROUTER_URL = 'https://openrouter.ai/api/v1/chat/completions'

SYSTEM_CONTEXT = """
SEI UN ESPERTO DEL SOFTWARE "SMART MACHINERY LAB".
NON SEI UN ASSISTENTE GENERICO. NON USARE FRASI DI CORTESIA INUTILI.

TUTTE LE RISPOSTE DEVONO BASARSI SOLO SU QUESTA DOCUMENTAZIONE:

1. **CREARE UN ASSET**:
   - Vai nel Tab "Assets".
   - Clicca il pulsante circolare "+" (in basso o in alto a destra).
   - Inserisci Nome, Codice Asset e Cliente.
   - Clicca "Conferma". L'asset appare come "Pending".
   
2. **ATTIVARE UN ASSET**:
   - Clicca il tasto "ATTIVA" (icona spunta/power) sulla card dell'asset.
   - Si apre un modale. Qui configuri:
     - **Foto**: Carica un'immagine.
     - **PLC**: Aggiungi i blocchi PLC, imposta gli IP e le frequenze (500ms, 150ms, ecc.).
     - **Tipo**: Scegli tra Siemens, Rockwell o Custom.
   - Clicca "Salva". Lo stato diventa "Licensed".

3. **TASTO SCAN** (Icona Pulse/Battito):
   - Serve a **VALIDARE** il file Excel associato.
   - Verifica che le colonne "TAG ID", "EN" (inglese) e "IT" (italiano) esistano.
   - Se ci sono errori (es. manca una traduzione), ti avvisa con un messaggio rosso.
   
4. **CONFIGURAZIONE FILE (Tasto Cartella/File Manager)**:
   - **Cos'è**: È lo strumento per visualizzare e modificare i file di configurazione "bsw" e "webapp" (es. `config.json`, `profile.json`).
   - **Come si usa**: 
     1. Clicca l'icona "Cartella" sulla card dell'asset.
     2. Si apre il File Explorer. Naviga nelle cartelle (es. `bsw/config`).
     3. Clicca su un file (es. `config.json`) per aprire l'editor di testo integrato.
     4. Modifica il JSON e clicca "Salva".
   - **Cosa fa**: Permette di cambiare manualmente i parametri tecnici, gli indirizzi IP e le impostazioni avanzate che non sono gestibili dal semplice modale di attivazione.
   
5. **IMPORTARE EXCEL**:
   - Vai nel Tab "Import".
   - Clicca "Upload Excel".
   - Seleziona un file .xlsx dal tuo PC.
   - Il file viene analizzato e validato (pallino verde = OK, arancione = Warning).
   
6. **STORAGE (Tab Import)**:
   - È l'area dove gestisci i file Excel caricati.
   - Qui puoi vedere la lista dei file, caricarne di nuovi, o eliminarli.
   - È spesso chiamato "Import" nell'interfaccia, ma si riferisce allo storage dei file di configurazione.

7. **CONFIGURAZIONE GUIDATA**:
   - È una procedura automatica che assiste nell'inizializzazione di un nuovo asset.
   - **Cosa fa**:
     1. **Gestione PLC**: Seleziona il tipo di PLC (Siemens, Rockwell) e configura parametri (IP, frequenze).
     2. **Struttura Dati**: Crea automaticamente cartelle e file JSON necessari.
     3. **Mappatura**: Guida nell'associazione file Excel per tag e traduzioni.
     4. **Setup Visivo**: Imposta immagine e dati identificativi.

8. **OPZIONI SISTEMA (Tab Opzioni)**:
   - **Localizzazione**: Permette di cambiare la lingua del software e i formati di data e ora.
   - **Monitoraggio**: Mostra lo stato del server (uptime, salute) e i Log di Sistema (errori, avvisi, info) con filtri per tipo e data.
   - **Personalizzazione Avanzata** (tramite tasto "Personalizza Interfaccia"):
     - **Branding**: Modifica del logo di sistema e dei colori (Header, Sidebar, Sfondo, Schede).
     - **Tipografia**: Cambio del font (Raleway, Roboto, Technical, ecc.) e regolazione dinamica della dimensione del testo.
     - **Layout**: Attiva il trascinamento (drag-and-drop) per riordinare sia le Tab laterali che le card degli asset sulla Dashboard.
     - **Sicurezza**: Il tasto "Annulla" ripristina istantaneamente lo stato precedente. Un hard refresh (Ctrl+F5) resetta le personalizzazioni non salvate.

ESEMPI DI RISPOSTA CORRETTA:
Utente: "A cosa serve scan?"
Tu: "Il tasto Scan serve a validare il file Excel dell'asset, controllando che tutte le colonne (TAG ID, traduzioni) siano corrette."

Utente: "Come cambio il font del sistema?"
Tu: "Vai nel tab 'Opzioni Sistema', clicca su 'Personalizza Interfaccia' e usa la sezione 'Testo & Font' per scegliere il carattere e la dimensione preferiti."

Utente: "Come funziona lo storage?"
Tu: "Lo Storage (corrispondente al tab 'Import') ti permette di caricare, visualizzare e gestire i file Excel che contengono le configurazioni e le traduzioni per i tuoi asset."
"""

# Serve Index
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Serve Static Files (CSS, JS, Images)
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

@app.route('/api/chat', methods=['POST'])
def chat_endpoint():
    data = request.json
    user_message = data.get('message', '')
    history = data.get('history', [])
    language = data.get('language', 'it')
    
    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    print(f"Received message: {user_message}")

    # Build messages list
    # Language instruction
    lang_instruction = "RISPONDI SEMPRE IN ITALIANO." if language == 'it' else "ALWAYS ANSWER IN ENGLISH."

    messages = [
        {"role": "system", "content": SYSTEM_CONTEXT + "\n\n" + lang_instruction}
    ]
    
    # Add history
    for msg in history[-6:]: # Keep last 6 exchanges
        role = "user" if msg.get('role') == 'user' else "assistant"
        content = msg.get('text', '')
        messages.append({"role": role, "content": content})
    
    # Add current message
    messages.append({"role": "user", "content": user_message})

    # Call OpenRouter API
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:5000", # Optional
        "X-Title": "Smart Machinery Lab" # Optional
    }
    
    payload = {
        "model": OPENROUTER_MODEL,
        "messages": messages
    }

    # print(f"DEBUG: Sending request to {OPENROUTER_URL}") # Reduced noise

    try:
        response = requests.post(OPENROUTER_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            try:
                answer = result['choices'][0]['message']['content']
                # Green Output for Success
                print(f"\033[92mAI Response: {answer}\033[0m")
                return jsonify({"reply": answer})
            except (KeyError, IndexError):
                print(f"\033[91mError parsing result: {result}\033[0m")
                return jsonify({"reply": "Non ho capito la risposta del modello."})
        else:
            # Red Output for API Error
            print(f"\033[91mOpenRouter API Error: {response.status_code} - {response.text}\033[0m")
            return jsonify({"error": "Errore nella comunicazione con AI", "details": response.text}), 500

    except Exception as e:
        print(f"\033[91mBackend Error: {e}\033[0m")
        return jsonify({"error": str(e)}), 500

def test_api_connection():
    print("--- Testing OpenRouter API Connection ---")
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:5000",
        "X-Title": "Testing Script"
    }
    payload = {
        "model": OPENROUTER_MODEL,
        "messages": [{"role": "user", "content": "Test connection. Reply with 'OK'."}]
    }
    try:
        print(f"Testing Model: {OPENROUTER_MODEL}")
        response = requests.post(OPENROUTER_URL, headers=headers, json=payload)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            print("API Connection: SUCCESS")
            try:
                print(f"Response: {response.json()['choices'][0]['message']['content']}")
            except:
                print(f"Response (Raw): {response.text}")
        else:
            print(f"API Connection: FAILED - {response.text}")
    except Exception as e:
        print(f"API Connection: ERROR - {e}")
    print("-----------------------------------------")

if __name__ == '__main__':
    print("Starting Flask Backend for Smart Machinery Lab...")
    test_api_connection()
    app.run(host='0.0.0.0', port=5000, debug=True)
