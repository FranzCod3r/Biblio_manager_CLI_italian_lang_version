\# 📚 Gestione Biblioteca

Un semplice gestionale da riga di comando scritto in \*\*Python\*\* per simulare la gestione di una piccola biblioteca. 

Permette di caricare libri da file CSV, visualizzare il catalogo e gestire i prestiti.


---


\## Funzionalità attuali

\- Caricamento libri da `data/libri.csv`

\- Visualizzazione catalogo libri

\- Prestito di un libro a un utente demo

\- Aggiornamento automatico del CSV dopo un prestito


---

\## 🛠️ Stato del progetto

Questo progetto è \*\*work in progress\*\*.  

Al momento sono implementate solo le prime funzioni di base (menu con 3 voci).  

In roadmap ci sono:

\- \[ ] Gestione utenti da CSV (`data/utenti.csv`)

\- \[ ] Inserimento nuovi utenti dal menu

\- \[ ] Inserimento nuovi libri dal menu

\- \[ ] Ricerca dettagli utente per ID

\- \[ ] Restituzione libri e storico prestiti


---

\## 📂 Struttura del progetto

gestione-biblioteca/  

├── main.py  # entry point con menu CLI 

├── src/    

    ├── models.py  # classi Libro, Utente, Prestito │   

    ├── storage.py # funzioni per caricare/salvare CSV │    

├──data/

    ├── libri.csv  # catalogo libri 

    └── utenti.csv # elenco utenti (in futuro)

├──tests/

    ├── test\_models.py

    └── test\_storage.py

---



\## 📦 Requisiti

\- Python 3.10+

\- Moduli standard (`csv`, `pathlib`)



--

\## ▶️ Utilizzo

Clona il repository e avvia il programma:

```bash

git clone https://github.com/<tuo-utente>/gestione-biblioteca.git

cd gestione-biblioteca

python main.py



1\. Mostra libri

2\. Presta libro

3\. Esci



