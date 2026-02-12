const translations = {
    it: {
        // Sidebar & Nav
        "nav.assets": "Assets",
        "nav.chatbot": "Chatbot",
        "nav.storage": "Storage",
        "nav.systemOptions": "Opzioni Sistema",
        "nav.docs": "Documentazione",
        "nav.back": "Indietro",
        "nav.analysis": "Analisi Dati",
        "nav.logout": "Logout",

        // Login & Welcome
        "login.title": "Smart Machinery Lab",
        "login.subtitle": "Sistema di gestione dati",
        "login.username": "Nome utente",
        "login.password": "Password",
        "login.button": "Accedi",
        "welcome.title": "Benvenuto!",
        "welcome.subtitle": "Smart Machinery Lab Dashboard",

        // Assets Tab
        "assets.title": "Gestione Assets",
        "assets.add": "Aggiungi un asset",
        "assets.deleteMsg": "Sei sicuro di voler eliminare questa macchina?",
        "assets.deleteTitle": "Conferma Eliminazione",
        "assets.cancel": "Annulla",
        "assets.delete": "Elimina",
        "assets.createModal.title": "Crea Asset",
        "assets.createModal.nameLabel": "Nome Asset:",
        "assets.createModal.namePlaceholder": "Es: Pressa 1",
        "assets.createModal.codeLabel": "Sigla asset (opzionale):",
        "assets.createModal.codePlaceholder": "Es: MCH-001",
        "assets.createModal.orderLabel": "MAA1 (Commessa) (opzionale):",
        "assets.createModal.orderPlaceholder": "Es: 123456",
        "assets.createModal.clientLabel": "Cliente (opzionale):",
        "assets.createModal.clientPlaceholder": "Es: Presezzi",
        "assets.createModal.btnCreate": "Crea Asset",
        "assets.createModal.btnCancel": "Annulla",
        "client.select": "Seleziona Cliente",
        "client.addNew": "Aggiungi nuovo cliente...",
        "client.enterNew": "Inserisci nuovo cliente",
        "activation.title": "Configurazione Macchina",
        "activation.imageLabel": "Immagine Asset",
        "activation.imagePlaceholder": "Trascina o clicca per caricare una foto",
        "activation.plcTypeLabel": "Tipologia PLC",
        "activation.plcOther": "Altro",
        "activation.addPlc": "Aggiungi PLC",
        "activation.dbCodeLabel": "Codice Database",
        "activation.dbPlaceholder": "MCC",
        "activation.excelLabel": "Associazione Excel",
        "activation.uploadExcel": "Carica Nuovo Excel",
        "activation.saveBtn": "Salva Configurazione",
        "activation.plcConfig": "CONFIGURAZIONE PLC {0}",
        "activation.ipLabel": "INDIRIZZO IP",
        "activation.ipPlaceholder": "Esempio: 192.168.1.11",
        "activation.freqLabel": "FREQUENZA DI CAMPIONAMENTO (MULTIPLE)",
        "activation.plcRockwell": "RockWell",
        "activation.plcSiemens": "Siemens",
        "script.file": "File",
        "script.delete": "Rimuovi",
        "script.changeExcel": "Cambia Excel",
        "fm.title": "File di Configurazione",
        "fm.newFolder": "Nuova Cartella",
        "fm.searchPlaceholder": "Cerca file...",

        // Storage/Import Tab
        "storage.title": "Import File Excel",
        "storage.upload": "Carica File",
        "storage.filesTitle": "File caricati",
        "storage.createGroup": "Crea Gruppo",
        "storage.view": "Visualizza Excel",
        "storage.delete": "Elimina",
        "storage.listAll": "List all",
        "storage.edit": "Modifica",
        "storage.export": "Esporta",
        "storage.zoomIn": "Ingrandisci",
        "storage.zoomOut": "Riduci",
        "storage.close": "Chiudi",
        "storage.save": "Salva Modifiche",
        "storage.sheet": "Foglio:",
        "storage.noExcel": "Nessun file Excel associato",
        "storage.assign": "Seleziona File Excel",

        // Chatbot Tab
        "chatbot.title": "Chatbot Assistente",
        "chatbot.subtitle": "Fai una domanda e riceverai una risposta",
        "chatbot.placeholder": "Scrivi un messaggio...",
        "chatbot.send": "Invia",
        "chatbot.welcome": "Ciao! Sono il tuo assistente virtuale. Come posso aiutarti oggi?",

        // System Options Tab
        "options.title": "Opzioni di Sistema",
        "options.language": "Lingua / Language",
        "options.theme": "Tema",
        "options.save": "Salva Opzioni",
        "options.saved": "Opzioni Salvate!",
        "options.systemLog": "Log di Sistema",
        "options.serverStatus": "Stato Server / Uptime",
        "options.dateFormat": "Formato Data / Ora",
        "options.dashboardLayout": "Layout Dashboard",
        "options.editLayout": "Personalizza Widget",
        "options.uptime": "Uptime Totale",
        "options.health": "Salute Sistema",
        "options.logType": "Tipo",
        "options.logDate": "Data/Ora",
        "options.logEvent": "Evento",
        "options.statusOnline": "Online",
        "options.lastDowntime": "Ultimo Downtime",
        "options.changeLogo": "Cambia Logo Sistema",
        "options.logoPreview": "Anteprima Logo",
        "options.customizeColors": "Personalizzazione Colori",
        "options.colorPrimary": "Colore Primario",
        "options.colorHeader": "Sfondo Header",
        "options.colorSidebar": "Sfondo Sidebar",
        "options.colorText": "Colore Testo",
        "options.colorBg": "Sfondo Applicazione",
        "options.colorCards": "Sfondo Schede",
        "options.textSettings": "Testo & Font",
        "options.fontFamily": "Carattere",
        "options.fontSize": "Dimensione Testo",
        "options.editTabs": "Riordina Tab Laterali",
        "options.resetLayout": "Ripristina Layout Default",


        "script.bswGenerated": "Configurazione BSW generata!",
        "script.genError": "Errore durante la generazione.",
        "script.redisName": "Qual è il nome del redis?",
        "script.associateExcelBefore20ms": "Associa un file Excel all'asset prima di procedere con la configurazione 20ms/50ms.",
        "script.pageNotFoundForFreq": "Impossibile trovare una pagina nell'Excel che contenga '{0}' per estrarre i Tag.",
        "script.noDataInPage": "Nessun dato trovato nella pagina \"{0}\" dell'Excel.",
        "script.selectBufferIndex": "[{0}ms] Seleziona bufferIndexTagId",
        "script.selectBufferBase": "[{0}ms] Seleziona buffersTagId (Base)",
        "script.bufferProfileGenerated": "Profilo Buffer Layout ({0}ms) generato correttamente con {1} gruppi.",
        "script.profileGenerated": "Profilo {0} generato correttamente!",
        "script.confirmIp": "Confermi che l'indirizzo IP è questo {0}?",
        "script.askIp": "Qual è l'IP del PLC?",
        "script.errorNoExcel": "Errore: Nessun file Excel associato all'asset.",
        "script.errorPageNotFound": "Errore: Pagina con frequenza \"{0}\" non trovata nell'Excel.",
        "script.profileSuccess": "Profilo {0} generato con successo dalle pagine: {1} ({2} parametri).",
        "script.folderName": "Nome cartella:",
        "script.newFolder": "Nuova Cartella",
        "script.errorRoot": "Errore: Root mancante.",
        "script.errorNoConfig": "Errore: Configurazione non caricata.",
        "script.renameBox": "Rinomina Box:",
        "script.noExcelLoaded": "Nessun file Excel caricato. Vai al tab Import e carica un file prima.",
        "script.allOk": "✅ Tutto OK!",
        "script.close": "Chiudi",
        "script.save": "Salva",
        "script.edit": "Modifica",
        "script.assetPending": "Start Licensing",
        "script.assetLicensed": "Licensed",

        // Modals & Common
        "modal.confirm": "Conferma",
        "modal.cancel": "Annulla",
        "common.saved": "Salvato!",
        "modal.createBox": "Crea Asset",
        "modal.boxName": "Nome Asset:",
        "modal.assetCode": "Sigla asset (opzionale):",
        "modal.orderNumber": "MAA1 (Commessa) (opzionale):",
        "modal.client": "Cliente (opzionale):",
        "modal.plcConfig": "Configurazione Macchina",
        "modal.plcType": "Tipologia PLC",
        "modal.assetImage": "Immagine Asset",
        "modal.addPlc": "Aggiungi PLC",
        "modal.saveConfig": "Salva Configurazione",
        "modal.dbCode": "Codice Database",
        "modal.selectExcel": "Seleziona File Excel",
        "modal.uploadNew": "Carica Nuovo Excel",

        "modal.selectExcel": "Seleziona File Excel",
        "modal.uploadNew": "Carica Nuovo Excel",

        // Documentation Section
        "docs.title": "Documentazione",
        "docs.subtitle": "Guida all'uso di Smart Machinery Lab",
        "docs.content": `
<div class="docs-section">
    <div class="docs-block">
        <h3 class="docs-title">1. Gestione Asset</h3>
        <p class="docs-text">Il modulo <b>Assets</b> è il cuore del sistema. Qui puoi configurare le macchine e i loro parametri di comunicazione.</p>
        
        <h4>Creazione Nuovo Asset</h4>
        <ul>
            <li>Clicca il pulsante <b>"+ Aggiungi un asset"</b>.</li>
            <li>Compila i campi richiesti: <b>Nome Asset</b>, <b>Codice</b> e <b>Cliente</b>.</li>
            <li>Conferma per creare l'asset in stato "Pending".</li>
        </ul>

        <h4>Attivazione e Licenza</h4>
        <ul>
            <li>Clicca l'icona <b style="color:var(--primary-red);">ATTIVA</b> sulla card dell'asset.</li>
            <li>Configura i <b>PLC</b> (Siemens, Rockwell) definendo IP e frequenze di campionamento.</li>
            <li>Salva la configurazione. Lo stato passerà a "Licensed" e verranno generati i file di sistema.</li>
        </ul>
        
        <div class="docs-note">
            <span class="docs-icon-container">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="docs-icon">
                    <circle cx="12" cy="12" r="10"></circle>
                    <line x1="12" y1="16" x2="12" y2="12"></line>
                    <line x1="12" y1="8" x2="12.01" y2="8"></line>
                </svg>
            </span>
            <div><b>Nota:</b> È fondamentale configurare correttamente gli IP dei PLC per garantire la comunicazione con il campo.</div>
        </div>
    </div>

    <div class="docs-block">
        <h3 class="docs-title">2. Validazione Dati (Scan)</h3>
        <p class="docs-text">La funzione <b>Scan</b> garantisce l'integrità dei dati importati.</p>
        <ul>
            <li>Clicca l'icona <b>Scan</b> (Battito cardiaco) sulla card.</li>
            <li>Il sistema verifica la presenza del file Excel associato.</li>
            <li>Vengono controllate le colonne obbligatorie: <span class="docs-code">TAG ID</span>, <span class="docs-code">IT</span>, <span class="docs-code">EN</span>.</li>
            <li>Eventuali errori verranno segnalati per la correzione immediata.</li>
        </ul>
    </div>

    <div class="docs-block">
        <h3 class="docs-title">3. File Manager Avanzato</h3>
        <p class="docs-text">Accedi ai file di configurazione diretti senza uscire dalla dashboard.</p>
        <ul>
            <li>Usa l'icona <b>Cartella</b> per aprire il File Manager.</li>
            <li>Naviga tra le cartelle generate (es. <span class="docs-code">bsw</span>, <span class="docs-code">webapp</span>).</li>
            <li>Modifica i file JSON o Python direttamente nell'editor integrato.</li>
        </ul>
             <div class="docs-note warning">
            <span class="docs-icon-container">
                 <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="docs-icon">
                    <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
                    <line x1="12" y1="9" x2="12" y2="13"></line>
                    <line x1="12" y1="17" x2="12.01" y2="17"></line>
                </svg>
            </span>
            <div><b>Attenzione:</b> Modificare manualmente i file di configurazione può compromettere il funzionamento dell'asset se non si è esperti.</div>
        </div>
    </div>

    <div class="docs-block">
        <h3 class="docs-title">4. Importazione & Storage</h3>
        <p class="docs-text">Gestione centralizzata dei file di traduzione e configurazione.</p>
        <ul>
            <li>Carica nuovi file <b>.xlsx</b> tramite il pulsante "Carica File".</li>
            <li>Visualizza e modifica il contenuto dei fogli Excel direttamente nel browser.</li>
            <li>Crea gruppi di file per organizzare meglio i progetti complessi.</li>
        </ul>
    </div>
</div>
        `,

        // Validation/Internal
        "validation.results": "Risultati Validazione",
        "validation.ok": "OK",

        // Text from Script.js (Dynamic)
        "fm.deleteConfirm": "Sei sicuro di voler eliminare questo elemento?",
        "fm.rootDeleteError": "Impossibile eliminare la root.",
        "fm.renamePrompt": "Inserisci nuovo nome:",
        "scan.noExcel": "Nessun file Excel valido associato a \"{0}\".",
        "scan.missingWorkbook": "Dati workbook mancanti per questo file.",
        "scan.errorsFound": "Trovati {0} errori nel file Excel.",
        "scan.validItems": "({0} elementi validi salvati provvisoriamente)",
        "scan.goToStorage": "Vai nello STORAGE per correggere gli errori.",
        "scan.success": "Validazione superata!",
        "scan.ready": "{0} elementi pronti.",
        "scan.noData": "Nessun dato valido trovato nel file.",
        "scan.systemError": "Si è verificato un errore durante la scansione: ",
        "scan.completed": "Scansione Completata",
        "scan.attention": "Attenzione: Errori Rilevati",
        "scan.error": "Errore",
        "scan.noFg": "Nota: 'FUNCTIONAL GROUP' assente (Accettabile)",
        "scan.andMore": "...e altri {0}.",
        "automation.success": "Complimenti! Tutte le configurazioni sono complete.\n\nIl sistema è pronto.",
    },
    en: {
        // Sidebar & Nav
        "nav.assets": "Assets",
        "nav.chatbot": "Chatbot",
        "nav.storage": "Storage",
        "nav.systemOptions": "System Options",
        "nav.docs": "Documentation",
        "nav.back": "Back",
        "nav.analysis": "Data Analysis",
        "nav.logout": "Logout",

        // Login & Welcome
        "login.title": "Smart Machinery Lab",
        "login.subtitle": "Data Management System",
        "login.username": "Username",
        "login.password": "Password",
        "login.button": "Login",
        "welcome.title": "Welcome!",
        "welcome.subtitle": "Smart Machinery Lab Dashboard",

        // Assets Tab
        "assets.title": "Asset Management",
        "assets.add": "Add Asset",
        "assets.deleteMsg": "Are you sure you want to delete this machine?",
        "assets.deleteTitle": "Confirm Deletion",
        "assets.cancel": "Cancel",
        "assets.delete": "Delete",
        "assets.createModal.title": "Create Asset",
        "assets.createModal.nameLabel": "Asset Name:",
        "assets.createModal.namePlaceholder": "Ex: Press 1",
        "assets.createModal.codeLabel": "Asset Code (optional):",
        "assets.createModal.codePlaceholder": "Ex: MCH-001",
        "assets.createModal.orderLabel": "Order Number (optional):",
        "assets.createModal.orderPlaceholder": "Ex: 123456",
        "assets.createModal.clientLabel": "Client (optional):",
        "assets.createModal.clientPlaceholder": "Ex: Presezzi",
        "assets.createModal.btnCreate": "Create Asset",
        "assets.createModal.btnCancel": "Cancel",
        "client.select": "Select Client",
        "client.addNew": "Add new client...",
        "client.enterNew": "Enter new client name",
        "activation.title": "Machine Configuration",
        "activation.imageLabel": "Asset Image",
        "activation.imagePlaceholder": "Drag or click to upload a photo",
        "activation.plcTypeLabel": "PLC Type",
        "activation.plcOther": "Other",
        "activation.addPlc": "Add PLC",
        "activation.dbCodeLabel": "Database Code",
        "activation.dbPlaceholder": "MCC",
        "activation.excelLabel": "Excel Association",
        "activation.uploadExcel": "Upload New Excel",
        "activation.saveBtn": "Save Configuration",
        "activation.plcConfig": "PLC CONFIGURATION {0}",
        "activation.ipLabel": "IP ADDRESS",
        "activation.ipPlaceholder": "Example: 192.168.1.11",
        "activation.freqLabel": "SAMPLING FREQUENCY (MULTIPLE)",
        "activation.plcRockwell": "RockWell",
        "activation.plcSiemens": "Siemens",
        "script.file": "File",
        "script.delete": "Remove",
        "script.changeExcel": "Change Excel",
        "fm.title": "Configuration Files",
        "fm.newFolder": "New Folder",
        "fm.searchPlaceholder": "Search files...",

        // Storage/Import Tab
        "storage.title": "Import Excel File",
        "storage.upload": "Upload File",
        "storage.filesTitle": "Uploaded Files",
        "storage.createGroup": "Create Group",
        "storage.view": "View Excel",
        "storage.delete": "Delete",
        "storage.listAll": "List all",
        "storage.edit": "Edit",
        "storage.export": "Export",
        "storage.zoomIn": "Zoom In",
        "storage.zoomOut": "Zoom Out",
        "storage.close": "Close",
        "storage.save": "Save Changes",
        "storage.sheet": "Sheet:",
        "storage.noExcel": "No Excel file associated",
        "storage.assign": "Select Excel File",

        // Chatbot Tab
        "chatbot.title": "Assistant Chatbot",
        "chatbot.subtitle": "Ask a question and get an answer",
        "chatbot.placeholder": "Type a message...",
        "chatbot.send": "Send",
        "chatbot.welcome": "Hello! I am your virtual assistant. How can I help you today?",

        // System Options Tab
        "options.title": "System Options",
        "options.language": "Language",
        "options.theme": "Theme",
        "options.save": "Save Options",
        "options.saved": "Options Saved!",
        "options.systemLog": "System Log",
        "options.serverStatus": "Server Status / Uptime",
        "options.dateFormat": "Date / Time Format",
        "options.dashboardLayout": "Dashboard Layout",
        "options.editLayout": "Customize Widgets",
        "options.uptime": "Total Uptime",
        "options.health": "System Health",
        "options.logType": "Type",
        "options.logDate": "Date/Time",
        "options.logEvent": "Event",
        "options.statusOnline": "Online",
        "options.lastDowntime": "Last Downtime",
        "options.changeLogo": "Change System Logo",
        "options.logoPreview": "Logo Preview",
        "options.customizeColors": "Color Customization",
        "options.colorPrimary": "Primary Color",
        "options.colorHeader": "Header Background",
        "options.colorSidebar": "Sidebar Background",
        "options.colorText": "Text Color",
        "options.colorBg": "Application Background",
        "options.colorCards": "Card Background",
        "options.textSettings": "Text & Fonts",
        "options.fontFamily": "Font Family",
        "options.fontSize": "Text Size",
        "options.editTabs": "Reorder Lateral Tabs",
        "options.resetLayout": "Reset Default Layout",

        // Dynamic Script Messages
        "script.bswGenerated": "BSW Configuration Generated!",
        "script.genError": "Error during generation.",
        "script.redisName": "What is the redis name?",
        "script.associateExcelBefore20ms": "Associate an Excel file to the asset before proceeding with 20ms/50ms configuration.",
        "script.pageNotFoundForFreq": "Could not find a page in Excel containing '{0}' to extract Tags.",
        "script.noDataInPage": "No data found in Excel page \"{0}\".",
        "script.selectBufferIndex": "[{0}ms] Select bufferIndexTagId",
        "script.selectBufferBase": "[{0}ms] Select buffersTagId (Base)",
        "script.bufferProfileGenerated": "Buffer Layout Profile ({0}ms) generated correctly with {1} groups.",
        "script.profileGenerated": "{0} Profile generated correctly!",
        "script.confirmIp": "Confirm IP address is {0}?",
        "script.askIp": "What is the PLC IP?",
        "script.errorNoExcel": "Error: No Excel file associated with this asset.",
        "script.errorPageNotFound": "Error: Page with frequency \"{0}\" not found in Excel.",
        "script.profileSuccess": "{0} Profile generated successfully from sheets: {1} ({2} parameters).",
        "script.folderName": "Folder Name:",
        "script.newFolder": "New Folder",
        "script.errorRoot": "Error: Missing Root.",
        "script.errorNoConfig": "Error: Configuration not loaded.",
        "script.renameBox": "Rename Box:",
        "script.noExcelLoaded": "No Excel file loaded. Go to Import tab and upload one first.",
        "script.allOk": "✅ All OK!",
        "script.close": "Close",
        "script.save": "Save",
        "script.edit": "Edit",
        "script.assetPending": "Start Licensing",
        "script.assetLicensed": "Licensed",

        // Modals & Common
        "modal.confirm": "Confirm",
        "modal.cancel": "Cancel",
        "common.saved": "Saved!",
        "modal.createBox": "Create Asset",
        "modal.boxName": "Asset Name:",
        "modal.assetCode": "Asset Code (optional):",
        "modal.orderNumber": "MAA1 (Order) (optional):",
        "modal.client": "Client (optional):",
        "modal.plcConfig": "Machine Configuration",
        "modal.plcType": "PLC Type",
        "modal.assetImage": "Asset Image",
        "modal.addPlc": "Add PLC",
        "modal.saveConfig": "Save Configuration",
        "modal.dbCode": "Database Code",
        "modal.selectExcel": "Select Excel File",
        "modal.uploadNew": "Upload New Excel",

        "modal.selectExcel": "Select Excel File",
        "modal.uploadNew": "Upload New Excel",

        // Documentation Section
        "docs.title": "Documentation",
        "docs.subtitle": "Guide to using the Smart Machinery Lab",
        "docs.content": `
<div class="docs-section">
    <div class="docs-block">
        <h3 class="docs-title">1. Asset Management</h3>
        <p class="docs-text">The <b>Assets</b> module is the core of the system. Here you configure machines and their communication parameters.</p>
        
        <h4>Creating a New Asset</h4>
        <ul>
            <li>Click the <b>"+ Add Asset"</b> button.</li>
            <li>Fill in the required fields: <b>Asset Name</b>, <b>Code</b>, and <b>Client</b>.</li>
            <li>Confirm to create the asset in "Pending" status.</li>
        </ul>

        <h4>Activation & Licensing</h4>
        <ul>
            <li>Click the <b style="color:var(--primary-red);">ACTIVATE</b> icon on the asset card.</li>
            <li>Configure <b>PLCs</b> (Siemens, Rockwell) by defining IPs and sampling frequencies.</li>
            <li>Save the configuration. The status will change to "Licensed" and system files will be generated.</li>
        </ul>
        
        <div class="docs-note">
             <span class="docs-icon-container">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="docs-icon">
                    <circle cx="12" cy="12" r="10"></circle>
                    <line x1="12" y1="16" x2="12" y2="12"></line>
                    <line x1="12" y1="8" x2="12.01" y2="8"></line>
                </svg>
            </span>
            <div><b>Note:</b> Correctly configuring PLC IPs is critical ensuring field communication.</div>
        </div>
    </div>

    <div class="docs-block">
        <h3 class="docs-title">2. Data Validation (Scan)</h3>
        <p class="docs-text">The <b>Scan</b> function ensures the integrity of imported data.</p>
        <ul>
            <li>Click the <b>Scan</b> (Heartbeat) icon on the card.</li>
            <li>The system checks for the associated Excel file.</li>
            <li>Mandatory columns are verified: <span class="docs-code">TAG ID</span>, <span class="docs-code">IT</span>, <span class="docs-code">EN</span>.</li>
            <li>Any errors will be flagged for immediate correction.</li>
        </ul>
    </div>

    <div class="docs-block">
        <h3 class="docs-title">3. Advanced File Manager</h3>
        <p class="docs-text">Access configuration files directly without leaving the dashboard.</p>
        <ul>
            <li>Use the <b>Folder</b> icon to open the File Manager.</li>
            <li>Navigate through generated folders (e.g., <span class="docs-code">bsw</span>, <span class="docs-code">webapp</span>).</li>
            <li>Edit JSON or Python files directly in the integrated editor.</li>
        </ul>
             <div class="docs-note warning">
            <span class="docs-icon-container">
                 <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="docs-icon">
                    <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
                    <line x1="12" y1="9" x2="12" y2="13"></line>
                    <line x1="12" y1="17" x2="12.01" y2="17"></line>
                </svg>
            </span>
            <div><b>Warning:</b> Manually editing configuration files may compromise asset functionality if you are not an expert.</div>
        </div>
    </div>

    <div class="docs-block">
        <h3 class="docs-title">4. Import & Storage</h3>
        <p class="docs-text">Centralized management of translation and configuration files.</p>
        <ul>
            <li>Upload new <b>.xlsx</b> files via the "Upload File" button.</li>
            <li>View and edit Excel sheet content directly in the browser.</li>
            <li>Create file groups to better organize complex projects.</li>
        </ul>
    </div>
</div>
        `,

        // Validation/Internal
        "validation.results": "Validation Results",
        "validation.ok": "OK",

        // Text from Script.js (Dynamic)
        "fm.deleteConfirm": "Are you sure you want to delete this item?",
        "fm.rootDeleteError": "Cannot delete root.",
        "fm.renamePrompt": "Enter new name:",
        "scan.noExcel": "No valid Excel file associated to \"{0}\".",
        "scan.missingWorkbook": "Workbook data missing for this file.",
        "scan.errorsFound": "Found {0} errors in Excel file.",
        "scan.validItems": "({0} valid items provisionally saved)",
        "scan.goToStorage": "Go to STORAGE to fix errors.",
        "scan.success": "Validation Passed!",
        "scan.ready": "{0} items ready.",
        "scan.noData": "No valid data found in file.",
        "scan.systemError": "System error during scan: ",
        "scan.completed": "Scan Completed",
        "scan.attention": "Attention: Errors Detected",
        "scan.error": "Error",
        "scan.noFg": "Note: 'FUNCTIONAL GROUP' missing (Acceptable)",
        "scan.andMore": "...and {0} others.",
        "automation.success": "Congratulations! All configurations complete.\n\nThe system is ready.",
    }
};

let currentLanguage = localStorage.getItem('appLanguage') || 'it';

function t(key, params = []) {
    if (!translations[currentLanguage]) return key;
    let text = translations[currentLanguage][key] || key;
    if (params && params.length > 0) {
        params.forEach((param, index) => {
            text = text.replace(`{${index}}`, param);
        });
    }
    return text;
}

function setLanguage(lang) {
    if (translations[lang]) {
        currentLanguage = lang;
        localStorage.setItem('appLanguage', lang);
        updateInterfaceLanguage();
        // Dispatch Event for script.js to re-render dynamic content
        window.dispatchEvent(new CustomEvent('languageChanged', { detail: lang }));
    }
}

function updateInterfaceLanguage() {
    // 1. Handle elements with data-i18n (Text Content)
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');

        // Handle input placeholders implicitly if it's an input
        if (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA') {
            if (key) {
                element.placeholder = t(key);
            }
        } else if (key) {
            // Text Content (preserving icons if possible)
            let textNode = null;
            // Find the first text node that is not empty
            for (let i = 0; i < element.childNodes.length; i++) {
                if (element.childNodes[i].nodeType === Node.TEXT_NODE && element.childNodes[i].nodeValue.trim() !== '') {
                    textNode = element.childNodes[i];
                    break;
                }
            }

            if (textNode) {
                textNode.nodeValue = " " + t(key) + " ";
            } else if (element.children.length === 0) {
                element.textContent = t(key);
            }
        }

        // Handle explicit placeholder translation via data-i18n-placeholder attribute
        const placeholderKey = element.getAttribute('data-i18n-placeholder');
        if (placeholderKey && (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA')) {
            element.placeholder = t(placeholderKey);
        }
    });

    // 2. Separate pass for data-i18n-placeholder on elements that might NOT have data-i18n
    document.querySelectorAll('[data-i18n-placeholder]:not([data-i18n])').forEach(element => {
        const key = element.getAttribute('data-i18n-placeholder');
        if (key && (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA')) {
            element.placeholder = t(key);
        }
    });

    // Special handlers
    const chatInput = document.getElementById('chatbotInput');
    if (chatInput && !chatInput.hasAttribute('data-i18n-placeholder')) {
        chatInput.placeholder = t('chatbot.placeholder');
    }

    const welcomeTitle = document.querySelector('.welcome-title');
    if (welcomeTitle && !welcomeTitle.hasAttribute('data-i18n')) {
        welcomeTitle.textContent = t('welcome.title');
    }

    const welcomeSubtitle = document.querySelector('.welcome-subtitle');
    if (welcomeSubtitle && !welcomeSubtitle.hasAttribute('data-i18n')) {
        welcomeSubtitle.textContent = t('welcome.subtitle');
    }

    // Update Chatbot default welcome message if it's the only message
    const chatMsgs = document.getElementById('chatbotMessages');
    if (chatMsgs && chatMsgs.children.length === 1 && chatMsgs.children[0].classList.contains('bot-message')) {
        const p = chatMsgs.children[0].querySelector('p');
        if (p) p.textContent = t('chatbot.welcome');
    }

    // Link docs content
    const docsArea = document.getElementById('docsContentArea');
    if (docsArea) {
        docsArea.innerHTML = t('docs.content');
    }
}
