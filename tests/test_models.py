
# tests/test_models.py

import pytest

from src.models import Libro, Utente, Prestito

def test_libro_str():
    libro = Libro("1984", "Orwell", 1949, 3)
    assert "1984" in str(libro)
    assert "Orwell" in str(libro)

def test_prestito_dettagli():
    utente = Utente("Franz", 30, "U001")
    libro = Libro("1984", "Orwell", 1949, 3)
    prestito = Prestito(utente, libro, 7)
    dettagli = prestito.dettagli()
    assert "Franz" in dettagli
    assert "1984" in dettagli
    assert "7" in dettagli
