from metodySprawdzajace import czyDiagonalnieDominujaca, wyborWarunku, czyDodatnioOkreslona
import numpy as np

def metodaGaussaSeidla(macierz, wektor):
    if not czyDiagonalnieDominujaca(macierz) or not czyDodatnioOkreslona(macierz):
        print("Nie można zastosować metody Gaussa-Seidla dla wybranej macierzy- nie jest diagonalnie dominująca lub dodatnio określona.")
        return False

    row, col = macierz.shape
    rowW = wektor.shape[0]

    if row != col:
        print("Macierz nie jest kwadratowa- nie można zastosować metody Gaussa-Seidla.")
        return False

    if rowW != col:
        print("Wymiary macierzy i wektora nie zgadzają się- nie można zastosować metody Gaussa-Seidla.")
        print("roww", rowW)
        print("rcoool", col)
        return False

    print("Na wybranej macierz można zastosować metodę Gaussa-Seidla.")
    warunekStopu, iloscPrzejsc = wyborWarunku()

    xPoczatkowe = np.ones(rowW)

    x = xPoczatkowe.copy()

    if warunekStopu == "it":
        for przejscie in range(iloscPrzejsc):
            for i in range(rowW):
                sum = 0.
                for j in range(rowW):
                    if i != j:
                        sum += macierz[i, j] * x[j]
                x[i] = (wektor[i] - sum) / macierz[i, i]
        print(x)

    if warunekStopu == "dok":
        print("dokladnosc- do dopisania")