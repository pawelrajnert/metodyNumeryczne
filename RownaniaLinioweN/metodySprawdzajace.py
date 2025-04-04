import numpy as np


def wyborWarunku():
    print("Dostępne opcje warunku stopu: ")
    print("1) dokładność obliczeń według wzoru |xi − xi−1| < ε")
    print("2) podana ilość iteracji")
    while True:
        wybor = int(input("Wybierz warunek stopu: "))
        if wybor == 1:
            eps = float(input("Wprowadź wartość e: "))
            if eps > 0:
                return ("dok", eps)
            else:
                print("Nieprawidłowa wartość epsilonu!")
        elif wybor == 2:
            iteracje = int(input("Wprowadź ilość iteracji: "))
            if iteracje > 0:
                return ("it", iteracje)
            else:
                print("Wprowadzono niepoprawną ilość iteracji.")
        else:
            print("Wybrano błędną opcję!")


# Warunek działania metody Gaussa-Seidla- sprawdzenie czy macierz jest diagonalnie dominująca.
# Metoda zwraca prawidłową kolejność ułożenia wierszy w macierzy,
# a jeśli macierz nie jest diagonalnie dominująca, to zwraca None
def czyDiagonalnieDominujaca(macierz):
    unikalneIndeksyMaksimum = set()
    kolejnosc = list()
    row, col = macierz.shape
    for i in range(row):
        maksimum = np.max(abs(macierz[i, :]))
        resztaMacierzy = np.sum(abs(macierz[i, :])) - maksimum

        if maksimum <= resztaMacierzy:
            return None

        for j in range(col):
            if maksimum == abs(macierz[i][j]):
                kolejnosc.append(j)
                unikalneIndeksyMaksimum.add(j)

    if len(unikalneIndeksyMaksimum) < row: return None
    return kolejnosc

# Przestawianie wierszy macierzy i wektora według kolejności zwróconej przez metodę powyżej
def zamienKolejnosc(macierz, wektor, kolejnosc):
    j = 0
    macierzKopia = np.copy(macierz)
    wektorKopia = np.copy(wektor)
    for i in kolejnosc:
        macierz[i, :] = macierzKopia[j, :]
        wektor[i] = wektorKopia[j]
        j += 1
    return macierz, wektor

# funkcja dla przykładów z pliku tekstowego o wynikach nieoznacoznych i sprzecznych
def diagonalnaDominacjaPom(macierz):
    row, col = macierz.shape
    for i in range(row):
        diagonala = abs(macierz[i, i])
        resztaMacierzy = 0

        for j in range(col):
            if i != j:
                resztaMacierzy += abs(macierz[i, j])

        if diagonala < resztaMacierzy:
            return False

    return True