from metodySprawdzajace import *
from metodaIGS import *
import numpy as np

print("Program do rozwiązywania układów N równań liniowych z N niewiadomymi\n")

while 1:
    print("1)   [3 3 1] [x1]   [12]\n"
          "     [2 5 7] [x2] = [33]\n"
          "     [1 2 1] [x3]   [8]\n"
          "(x1 = 1, x2 = 2, x3 = 3)\n")

    print("2)   [3   3    1]  [x1]   [ 1]\n"
          "     [2   5    7]  [x2] = [ 20]\n"
          "     [-4 -10 -14]  [x3]   [-40]\n"
          "(układ nieoznaczony)\n")

    print("3)   [3   3    1]  [x1]   [ 1]\n"
          "     [2   5    7]  [x2] = [ 20]\n"
          "     [-4 -10 -14]  [x3]   [-20]\n"
          "(układ sprzeczny)\n")

    print("4)   [ 0,5     -0.0625 0.1875  0.0625]  [x1]   [ 1,5]\n"
          "     [-0.0625   0.5     0      0]       [x2] = [-1,625]\n"
          "     [ 0.1875   0      0.375   0.125]   [x3]   [ 1]\n"
          "     [ 0.0625   0      0.125   0.25]    [x4]   [ 0,4375]\n"
          "(x1 = 2, x2 = -3, x3 = 1.5, x4 = 0.5)\n")

    print("5)   [3  2 1 -1]  [x1]   [ 0]\n"
          "     [5 -1 1  2]  [x2] = [-4]\n"
          "     [1 -1 1  2]  [x3]   [ 4]\n"
          "     [7  8 1 -7]  [x4]   [ 6]\n"
          "(układ sprzeczny)\n")

    print("6)   [ 3 -1  2 -1]  [x1]   [-13]\n"
          "     [ 3 -1  1  1]  [x2] = [ 1]\n"
          "     [ 1  2 -1  2]  [x3]   [ 21]\n"
          "     [-1  1 -2 -3]  [x4]   [-5]\n"
          "(x1 = 1, x2 = 3, x3 = -4, x4 = 5)\n")

    print("7)   [0 0 1]  [x1]   [3]\n"
          "     [1 0 0]  [x2] = [7]\n"
          "     [0 1 0]  [x3]   [5]\n"
          "(x1 = 7, x2 = 5, x3 = 3)\n")

    print("8)   [10 -5  1]  [x1]   [3]\n"
          "     [4  -7  2]  [x2] = [-4]\n"
          "     [5   1  4]  [x3]   [ 19]\n"
          "(x1 = 1, x2 = 2, x3 = 3)\n")

    print("9)   [ 6  -4   2]    [x1]   [4]\n"
          "     [-5   5   2]    [x2] = [11]\n"
          "     [ 0.9 0.9 3.6]  [x3]   [13.5]\n"
          "(układ nieoznaczony)\n")

    print("10)   [ 1    0.2  0.3]  [x1]   [1.5]\n"
          "      [ 0.1  1   -0.3]  [x2] = [0.8]\n"
          "      [-0.1 -0.2  1]    [x3]   [0.7]\n"
          "(x1 = 1, x2 = 1, x3 = 1)\n")

    print("0) - wczytanie współczynników z pliku wsłasneWspółczynniki.txt\n")

    menu = int(input("Wybierz opcję: "))
    wybranoMetode = True
    if menu == 1:
        macierz = np.array([
            [3, 3, 1],
            [2, 5, 7],
            [1, 2, 1]
        ], dtype=float)
        wektor = np.array([12, 33, 8], dtype=float)

    elif menu == 2:
        macierz = np.array([
            [3, 3, 1],
            [2, 5, 7],
            [-4, -10, -14]
        ], dtype=float)
        wektor = np.array([1, 20, -40], dtype=float)

    elif menu == 3:
        macierz = np.array([
            [3, 3, 1],
            [2, 5, 7],
            [-4, -10, -14]
        ], dtype=float)
        wektor = np.array([1, 20, -20], dtype=float)

    elif menu == 4:
        macierz = np.array([
            [0.5, -0.0625, 0.1875, 0.0625],
            [-0.0625, 0.5, 0, 0],
            [0.1875, 0, 0.375, 0.125],
            [0.0625, 0, 0.125, 0.25]
        ], dtype=float)
        wektor = np.array([1.5, -1.625, 1, 0.4375], dtype=float)

    elif menu == 5:
        macierz = np.array([
            [3, 2, 1, -1],
            [5, -1, 1, 2],
            [1, -1, 1, 2],
            [7, 8, 1, -7]
        ], dtype=float)
        wektor = np.array([0, -4, 4, 6], dtype=float)

    elif menu == 6:
        macierz = np.array([
            [3, -1, 2, -1],
            [3, -1, 1, 1],
            [1, 2, -1, 2],
            [-1, 1, -2, -3]
        ], dtype=float)
        wektor = np.array([-13, 1, 21, -5], dtype=float)

    elif menu == 7:
        # macierz = np.array([
        # [0, 0, 1],
        # [1, 0, 0],
        # [0, 1, 0]
        # ], dtype=float)

        # wektor = np.array([3, 7, 5], dtype=float)

        # wersja po zamianie wierszy (mozliwa do rozwiazania, bo jest diagonalnie dominująca)

        macierz = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ], dtype=float)

        wektor = np.array([7, 5, 3], dtype=float)

    elif menu == 8:
        macierz = np.array([
            [10, -5, 1],
            [4, -7, 2],
            [5, 1, 4]
        ], dtype=float)
        wektor = np.array([3, -4, 19], dtype=float)

    elif menu == 9:
        macierz = np.array([
            [6, -4, 2],
            [-5, 5, 2],
            [0.9, 0.9, 3.6]
        ], dtype=float)
        wektor = np.array([4, 11, 13.5], dtype=float)

    elif menu == 10:
        macierz = np.array([
            [1, 0.2, 0.3],
            [0.1, 1, -0.3],
            [-0.1, -0.2, 1]
        ], dtype=float)
        wektor = np.array([1.5, 0.8, 0.7], dtype=float)

    elif menu == 0:
        plik = np.loadtxt('własneWspółczynniki.txt', dtype=float, delimiter=';')
        macierz = plik[:, :-1]
        wektor = plik[:, -1]
        print
    else:
        wybranoMetode = False
        print("Błąd! Nie wybrano metody!")

    metodaGaussaSeidla(macierz, wektor)
    input("Aby kontynuować, naciśnij enter")
