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
def czyDiagonalnieDominujaca(macierz):
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


# Warunek działania metody Gaussa-Seidla- sprawdzenie czy macierz jest dodatnio określona.
def czyDodatnioOkreslona(macierz):
    return np.all(np.linalg.eigvals(macierz) > 0)
