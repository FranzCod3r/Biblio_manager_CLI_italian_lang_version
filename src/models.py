class Libro:
    """Rappresenta un oggetto Libro con titolo, autore, anno e copie disponibili."""

    def __init__(self, titolo, autore, anno, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili

    def info_libro(self):
        return f"{self.titolo} - {self.autore} ({self.anno}) | Copie: {self.copie_disponibili}"
    
    def __str__(self):
        # rappresentazione leggibile
        return f"{self.titolo} di {self.autore} ({self.anno})"


class Utente:
    def __init__(self, nome, eta, id_utente):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente

    def scheda(self):
        return f"{self.nome} - Età: {self.eta} - ID: {self.id_utente}"


class Prestito:
    def __init__(self, utente, libro, giorni):
        self.utente = utente
        self.libro = libro
        self.giorni = giorni

    def dettagli(self):
        return f"{self.utente.nome} ha preso '{self.libro.titolo}' per {self.giorni} giorni"