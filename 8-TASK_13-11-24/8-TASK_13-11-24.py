import random

#qui liste di generare/variazioni
generi = ["Rock", "Jazz", "Pop", "Metal", "Indie"]
aggettivi = ["Crazy", "crushed", "Misteriosi", "Incendiari", "Empty"]
strumenti = ["trombone", "clarinetto", "basso", "theremin", "Bbox"]
recensioni = [
    "Un nome accroccato per una band che proverà a conquisterà il mondo!",
    "Un fortuito mix che promette di lasciare il segno!",
    "Un nome ideale per una nuova era musicale. Speriamo!",
    "Il nome perfetto per i futuri idioti del genere!",
    "Un suono e un nome, cha altro possiamo dire!"
]
emoji = ["🤷", "🤶", "🤦", "🙉", "🦄"]

print("Ciao futura star!")

#qui raccogliamo i dati su l'umore dell'utente per personalizzare il saluto
umore = input("Come ti senti oggi? (felice, carico, pensieroso, etc.): ")
print(f"Wow, con questo mood '{umore}' andrà sicuramente bene, o forse NO!")

#qui raccogliamo le informazioni necessarie per creare il nome
city = input("In che città vivi? ")
pet = input("Come si chiama il tuo animaletto? ")

#qui scopriamo il genere musicale della band
genere = input(f"Indica il genere della tua band, tra questi elencati {generi}: ")

#qui scopriamo lo strumento del bandleader
strumento = input(f"Qual è lo strumento utilizzato dal Bandleader? Scegli tra questi {strumenti}: ")

#qui impostiamo l'ordine di preferenza
scelta = input("Vuoi che venga prima il nome della città(1) o quello del tuo animaletto(2)? Inserisci 1 o 2: ")

#qui andiamo a generare il nome della band
aggettivo = random.choice(aggettivi)
if scelta == "1":
    nome_band = f"{city} {aggettivo} {pet} - {genere} Band"
else:
    nome_band = f"{pet} {aggettivo} {city} - {genere} Band"

#qui definiamo la storia immaginaria della band
storia_band = f"Nata tra gli anfratti di {city} e ispirata dal {aggettivo} {pet}, la band ha deciso di vendere la propria anima al {genere}. \
Con il suo leader che padroneggia il {strumento}, {nome_band} è pronta a dominare il panorama musicale di serie D!"

#qui attribuiamo una recensione casuale
recensione = random.choice(recensioni)

#qui scegliamo una emoji casuale
emoji_scelta = random.choice(emoji)

#qui andiamo a mostrare a schermo il risultato finale
print(f"Fantastico, vi battezzo i {nome_band}")
print("\nStoria della band:")
print(storia_band)
print("\nRecensione della groupie (la mamma):")
print(f"{emoji_scelta} {recensione}")
