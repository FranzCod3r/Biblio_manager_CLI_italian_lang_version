# tests/test_storage.py

import csv
import tempfile
from pathlib import Path
from src.models import Libro
from src.storage import carica_libri_csv, salva_libri_csv

def test_salva_e_carica_libri():
    # creo un file temporaneo
    tmpfile = Path(tempfile.gettempdir()) / "libri_test.csv"
    libri = [Libro("1984", "Orwell", 1949, 3)]

    # salvo
    salva_libri_csv(libri, filename=tmpfile)

    # ricarico
    libri_caricati = carica_libri_csv(filename=tmpfile)

    assert len(libri_caricati) == 1
    assert libri_caricati[0].titolo == "1984"
    assert libri_caricati[0].autore == "Orwell"