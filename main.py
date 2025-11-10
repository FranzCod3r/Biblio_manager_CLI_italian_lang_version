from pathlib import Path
from src.models import Utente, Prestito, Libro
from src.storage import salva_libri_csv, carica_libri_csv

def menu():
    """Menù CLI interattivo"""
    print("\n--- Gestione Biblioteca ---")
    print("1. Mostra libri")
    print("2. Presta libro")
    print("3. Esci")

def main():
    #carico libri dal CSV - NB. aggiunti come oggetto Libro.
    libri = carica_libri_csv()

    #utente demo
    utente_demo = Utente("Luca", 30, "U0003")

    while True:
        menu()
        scelta = input("Cosa vuoi fare? seleziona una voce:")

        if scelta == "1":  #Mostra libri
            print("Catalogo Libri:")
            for libro in libri:
                print(libro.info_libro()) #Funzione presa da class Libro - models

        elif scelta == "2": #Presta libro
            titolo = input("Titolo del libro da prestare: ").lower().strip()
            giorni = int(input("Numero di giorni prestito: "))

            libro_trovato = next((l for l in libri if l.titolo.lower().strip() == titolo), None)
            if libro_trovato:
                if libro_trovato.copie_disponibili > 0:
                    libro_trovato.copie_disponibili -= 1
                    prestito = Prestito(utente_demo, libro_trovato, giorni)
                    print(prestito.dettagli())
                    salva_libri_csv(libri)  # aggiorno il CSV
                    
                else:
                    print("Nessuna copia disponibile!")
            else:
                print("Libro non trovato")
        
        #Exit Program    
        elif scelta == "3":
            print("Chiusura programma.")
            break

        else:
            print("Scelta non valida.")


if __name__ == "__main__":
    main()