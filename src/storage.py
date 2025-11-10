import csv
from src.models import Libro #aggiungere Utente e funzioni

def salva_libri_csv(libri, filename="data/libri.csv"):
    """salva nuovi oggetti Libro nel file .CSV"""

    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        fieldnames = ["titolo", "autore","anno", "copie_disponibili"]  #1. crea headers tabella csv
        writer = csv.DictWriter(f, fieldnames = fieldnames) #2. associo i fieldnames
        writer.writeheader() #3. scrive gli headers
        #loop per scrivere nel csv.
        for libro in libri: 
            writer.writerow({
                "titolo": libro.titolo,
                "autore": libro.autore,
                "anno": libro.anno,
                "copie_disponibili": libro.copie_disponibili
            })

def carica_libri_csv(filename="data/libri.csv"):
    """legge libri dal file csv e li aggiunge a lista 'libri' per riutilizzo nel programma"""
    libri = []
    with open(filename, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            libri.append(Libro(row["titolo"], row["autore"], int(row["anno"]), int(row["copie_disponibili"])))
    return libri


#aggiungere def per Utente - copiare logica da Libri - poi aggiornare il main