#qui importiamo il gozzziglione di funzioni per far funzionare il programma
import math
from colorama import Fore, Style, init
import matplotlib
matplotlib.use('TkAgg')  #backend per grafico compatibile su Kali Linux
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np  #per il calcolo numerico

#inizzializza colorama per il colore
init(autoreset=True)

# --> seguono i moduli per il calcolo degli spigoli <--
#qui calcola la somma degli spigoli del parallelepipedo
def calcola_spigoli_parallelepipedo():
    try:
        lunghezza = float(input("Inserisci il valore per la lunghezza del parallelepipedo: "))
        larghezza = float(input("Inserisci il valore per la larghezza del parallelepipedo: "))
        altezza = float(input("Inserisci il valore per l'altezza del parallelepipedo: "))
        if lunghezza <= 0 or larghezza <= 0 or altezza <= 0:
            print("AOOO: Il lato deve essere un numero superiore a 0 o positivo!")
            return
        somma_spigoli = 4 * (lunghezza + larghezza + altezza)
        print(f"La somma delle lunghezze degli spigoli del parallelepipedo è: {somma_spigoli}")
        grafico_parallelepipedo(lunghezza, larghezza, altezza)  #anche qui chiama la funzione per il grafico
    except ValueError:
        print("Annamo BENE: inserisci un numero valido, ti prego!")

#qui calcola la somma degli spigoli del cilindro
def calcola_spigoli_cilindro():
    try:
        raggio = float(input("Inserisci il valore per il raggio della base del cilindro: "))
        altezza = float(input("Inserisci il valore per l'altezza del cilindro: "))
        if raggio <= 0 or altezza <= 0:
            print("AOOO: Il lato deve essere un numero superiore a 0 o positivo!")
            return
        somma_spigoli = 4 * math.pi * raggio + 2 * altezza
        print(f"La somma delle lunghezze degli spigoli del cilindro è: {somma_spigoli}")
        grafico_cilindro(raggio, altezza)  #anche qui chiama la funzione per il grafico del cilindro
    except ValueError:
        print("EAnnamo BENE: inserisci un numero valido, ti prego!")

# --> seguono i moduli per i grafici <--
#qui crea un grafico 3D per il parallelepipedo
def grafico_parallelepipedo(lunghezza, larghezza, altezza):
    print(f"Generando il grafico per un parallelepipedo con lunghezza {lunghezza}, larghezza {larghezza}, altezza {altezza}...")  # Messaggio di debug
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    #punti di coordinata
    x = [0, lunghezza, lunghezza, 0, 0, 0, lunghezza, lunghezza, lunghezza, lunghezza]
    y = [0, 0, larghezza, larghezza, 0, 0, larghezza, larghezza, larghezza, larghezza]
    z = [0, 0, 0, 0, altezza, altezza, altezza, altezza, 0, 0]
    
    #grafico 3D
    ax.scatter(x, y, z, c='r')
    ax.plot_trisurf(x, y, z, color='c', alpha=0.3)
    plt.title("Parallelepipedo 3D")
    plt.show()

#qui crea un grafico 3D per il cilindro
def grafico_cilindro(raggio, altezza):
    print(f"Generando il grafico per un cilindro con raggio {raggio} e altezza {altezza}...")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    #valori
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, altezza, 100)
    x = raggio * np.outer(np.cos(u), np.ones_like(v))
    y = raggio * np.outer(np.sin(u), np.ones_like(v))
    z = np.outer(np.ones_like(u), v)
    
    #superficie
    ax.plot_surface(x, y, z, color='g', alpha=0.3)

    plt.title("Cilindro 3D")
    plt.show()

# --> seguono i moduli per le interazioni con l'utente <--
#qui la funzione principale
def main():
    #intro
    print(Fore.CYAN + "Benvenuto nel meraviglioso calcolatore di figure geometriche 3D della SNAZAH")
    print(Style.BRIGHT + "Questo accrocco di codice genera la somma delle lunghezze degli spigoli per le figure qui sotto selezionabili:")
    
    while True:
        print("\nChe figura ti stuzzica oggi:")
        print("1. Parallelepipedum (parallelepipedo, difficilissimo!)")
        print("2. Cylindrus (chi lo avrebbe mai detto! Un cilindro)")
        print("3. Ti ho stancato? Allora esci dal programma")

        scelta = input("Sei cortesemente pregato di digitare il numero corrispondente alla figura scelta: ")

        if scelta == "1":
            calcola_spigoli_parallelepipedo()
        elif scelta == "2":
            calcola_spigoli_cilindro()
        elif scelta == "3":
            break
        else:
            print("Con te mi arrendo. Puoi cortesemente scegliere un'opzione tra 1, 2 e 3!")
        
        ripeti = input("\nNon ti ho stancato? Allora vuoi calcolare un'altra figura? (s/n): ").lower()
        if ripeti != 's':
            break
    
    #outro
    print(Fore.GREEN + "\nGrazie per aver scelto la nostra compagnia aerea!")
    print("au revoir!")

#qui l'avvio del programma
if __name__ == "__main__":
    main()