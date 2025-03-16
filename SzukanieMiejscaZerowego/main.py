import matplotlib.pyplot as plt
from obliczenia import *
from metody import bisekcja, styczne


def wyborWarunku():
    print("Dostępne opcje warunku stopu: ")
    print("1) dokładność obliczeń według wzoru |xi − xi−1| < ε")
    print("2) podana ilość iteracji")
    while True:
        wybor = int(input("Wybierz warunek stopu: "))
        if wybor == 1:
            eps = float(input("Wprowadź wartość e: "))
            if eps > 0:
                return eps
            else:
                print("Nieprawidłowa wartość epsilonu!")
        elif wybor == 2:
            iteracje = int(input("Wprowadź ilość iteracji: "))
            if iteracje > 0:
                return iteracje
            else:
                print("Wprowadzono niepoprawną ilość iteracji.")
        else:
            print("Wybrano błędną opcję!")


def wykres(menu, start, stop, typ):
    x = np.linspace(start, stop)
    y = wartoscFunkcji(x, menu)
    w = wspolczynnikiFunkcji(menu)
    if menu == 1:
        plt.plot(x, y, label=f"{w[0]}x^3 + {w[1]}x^2 + {w[2]}x {w[3]}", linewidth=2)
    elif menu == 2:
        plt.plot(x, y, label=f"{w[0]}sin(x) + {w[1]}cos(x) - {abs(w[2])}", linewidth=2)
    elif menu == 3:
        plt.plot(x, y, label=f"{w[0]}^x - {abs(w[1])}", linewidth=2)
    elif menu == 4:
        plt.plot(x, y, label=f"{w[0]}sin(x) - {abs(w[1])}x^2 + {w[2]}^x", linewidth=2)
    if typ == 1:
        dodatkowyWykres()
    plt.axhline(0, color='black', linewidth=1)
    plt.legend()
    plt.show()


def dodatkowyWykres():
    yv1 = 0
    xv1, _ = bisekcja(x1, x2, menu, warunekStopu)
    xv2, _ = styczne(x1, x2, menu, warunekStopu)
    plt.plot(xv2, yv1, label="Metoda stycznych", marker="o", color="blue", markersize=15, fillstyle="none")
    plt.plot(xv1, yv1, label="Metoda bisekcji", marker="x", color="red", markersize=15, markeredgewidth=3)


print("Program do znajdywania miejsca zerowego równań nieliniowych metodami: bisekcji i stycznych.")

while 1:

    print("1) znajdywanie miejsca zerowego wielomianu ")
    print("2) znajdywanie miejsca zerowego funkcji trygonometrycznej ")
    print("3) znajdywanie miejsca zerowego funkcji wykładniczej ")
    print("4) znajdywanie miejsca zerowego złożenia funkcji ")

    menu = int(input("Wybierz opcję: "))
    wybranoMetode = True
    if menu == 1:
        print("Wybrano wielomian.")
        print("Wielomian jest w postaci: ")
        print("-x^3 + x^2 + 3x - 4 ")
        wykres(menu, -3, 3, 0)
    elif menu == 2:
        print("Wybrano funkcję trygonometryczną.")
        print("Funkcja trygonometryczna jest postaci: ")
        print("2sin(x) + 3cos(x) - 2")
        wykres(menu, -math.pi, math.pi, 0)
    elif menu == 3:
        print("Wybrano funkcję wykładniczą.")
        print("Funkcja wykładnicza jest postaci: ")
        print("2^x - 2")
        wykres(menu, -3, 3, 0)
    elif menu == 4:
        print("Wybrano złożenie funkcji.")
        print("Funkcja złożona jest postaci:")
        print("5sin(x) - 3x^2 + 2^x")
        wykres(menu, -5, 8, 0)
    else:
        wybranoMetode = False
        print("Błąd! Nie wybrano metody!")
    if wybranoMetode:
        warunekStopu = wyborWarunku()
        print("Podaj pierwszy koniec przedziału: ")
        x1 = float(input())
        print("Podaj drugi koniec przedziału: ")
        x2 = float(input())
        if x2 < x1:
            x1, x2 = x2, x1
        wynikBisekcja = bisekcja(x1, x2, menu, warunekStopu)
        wynikStyczne = styczne(x1, x2, menu, warunekStopu)
        if wynikBisekcja is not None and wynikStyczne is not None:
            print("Wynik metody bisekcji:", wynikBisekcja[0], "po liczbie iteracji:", wynikBisekcja[1])
            print("Wynik metody stycznych:", wynikStyczne[0], "po liczbie iteracji:", wynikStyczne[1])
            wykres(menu, x1, x2, 1)
