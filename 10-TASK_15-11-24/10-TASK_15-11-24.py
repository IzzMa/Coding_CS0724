import datetime

def data_oggi():
    oggi = datetime.date.today()
    return "La data di oggi è " + oggi.strftime("%d/%m/%Y")

def ora_attuale():
    ora = datetime.datetime.now().time()
    return "L'ora attuale è " + ora.strftime("%H:%M")

def nome_assistente():
    return "Mi chiamo Assistente Virtuale"

def assistente_virtuale(comando):
    #dizionario di comandi e funzioni
    comandi = {
        "data": data_oggi,
        "ore": ora_attuale,
        "nome": nome_assistente,
        "chiami": nome_assistente
    }
    
    #verifica se una delle parole chiave è nel comando
    for chiave, funzione in comandi.items():
        if chiave in comando:
            return funzione()  #esegue la funzione associata alla parola chiave
    
    #messaggio di errore se il comando non è riconosciuto
    return ("Comando non riconosciuto. "
            "Prova con: 'Qual è la data di oggi?', 'Che ore sono?', o 'Come ti chiami?'")

while True:
    try:
        comando_utente = input("Cosa vuoi sapere tra le opzioni sotto elencate? (digita 'esci' per uscire): \n"
                               "Qual è la data di oggi?, 'Che ore sono?', o 'Come ti chiami?'")
        if comando_utente.lower() == "esci":
            print("Arrivederci!")
            break
        else:
            print(assistente_virtuale(comando_utente.lower()))
    except Exception as e:
        print(f"Si è verificato un errore: {e}")
