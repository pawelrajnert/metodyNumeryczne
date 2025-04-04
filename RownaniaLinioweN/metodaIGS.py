from metodySprawdzajace import czyDiagonalnieDominujaca, wyborWarunku, zamienKolejnosc, diagonalnaDominacjaPom
import numpy as np


def metodaGaussaSeidla(macierz, wektor, pom):
    kolejnosc = 0
    if pom == 0:
        kolejnosc = czyDiagonalnieDominujaca(macierz)

    if kolejnosc is None and pom == 0:
        print("Nie można zastosować metody Gaussa-Seidla dla wybranej macierzy - nie jest diagonalnie dominująca.")
        return False

    if pom == 0:
        macierz, wektor = zamienKolejnosc(macierz, wektor, kolejnosc)

    if pom == 1:
        diagonalnaDominacjaPom(macierz)

    row, col = macierz.shape
    rowW = wektor.shape[0]
    if row != col:
        print("Macierz nie jest kwadratowa- nie można zastosować metody Gaussa-Seidla.")
        return False

    if rowW != col:
        print("Wymiary macierzy i wektora nie zgadzają się- nie można zastosować metody Gaussa-Seidla.")
        return False

    print("Na wybranej macierz można zastosować metodę Gaussa-Seidla.")
    warunekStopu, argument = wyborWarunku()

    xPoczatkowe = np.ones(rowW)

    if warunekStopu == "it":
        x = xPoczatkowe.copy()
        for przejscie in range(argument):
            for i in range(rowW):
                sum = 0.
                for j in range(rowW):
                    if i != j:
                        sum += macierz[i, j] * x[j]
                x[i] = (wektor[i] - sum) / macierz[i, i]
        print("Znalezione rozwiązanie: ", x)

    if warunekStopu == "dok":
        iteracjeDlaDokladnosci = 0
        x = xPoczatkowe.copy()
        while True:
            iteracjeDlaDokladnosci += 1
            xDlaPrzejscia = x.copy()
            for i in range(rowW):
                sum = 0.
                for j in range(rowW):
                    if i != j:
                        sum += macierz[i, j] * x[j]
                x[i] = (wektor[i] - sum) / macierz[i, i]
            print(x)
            if np.all(np.abs(x - xDlaPrzejscia) <= argument):
                break

        print("Znaleziono rozwiązanie po liczbie iteracji: ", iteracjeDlaDokladnosci, " - ", x)
