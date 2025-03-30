from metodaIGS import *
from metodySprawdzajace import czyDiagonalnieDominujaca, wyborWarunku


def metodaGaussaSeidla(macierz, wektor):
    if not czyDiagonalnieDominujaca(macierz):
        print("Nie można zastosować metody Gaussa-Seidla dla wybranej macierzy- nie jest diagonalnie dominująca")
        return False

    print("Na wybranej macierz można zastosować metodę Gaussa-Seidla.")
    warunekStopu = wyborWarunku()