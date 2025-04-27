from metody import *


def menu():
    print("Funkcja do interpolacji:")
    print("1) funkcja liniowa")
    print("2) moduł z x ")
    print("3) wielomian ")
    print("4) funkcja trygonometryczna ")
    print("5) złożenie funkcji ")
    print("6) funkcja testowa (efekt Rungego) ")

    menu = int(input("Wybierz opcję: "))
    wybranoMetode = True

    if menu == 1:
        print("Wybrano funkcję liniową.")
        print("Funkcja jest w postaci: ")
        print("2x + 6")
        f = liniowa


    elif menu == 2:
        print("Wybrano funkcję moduł z x.")
        print("Funkcja jest postaci: ")
        print("|x|")
        f = modul


    elif menu == 3:
        print("Wybrano wielomian.")
        print("Wielomian jest w postaci: ")
        print("-x^3 + x^2 + 3x - 4 ")
        f = wielomian


    elif menu == 4:
        print("Wybrano funkcję trygonometryczną.")
        print("Funkcja trygonometryczna jest postaci: ")
        print("2sin(x) + 3cos(x) - 2")
        f = trygonometryczna


    elif menu == 5:
        print("Wybrano złożenie funkcji.")
        print("Funkcja złożona jest postaci:")
        print("5sin(x) - 3x^2 + 2^x - |x| + 4")
        f = zlozenie

    elif menu == 6:
        print("Wybrano testową funkcję.")
        print("1/(1+25x^2)")
        f = testowa

    else:
        wybranoMetode = False
        print("Błąd! Nie wybrano metody!")

    if wybranoMetode:
        wykresPoczatkowy(f, -math.pi, math.pi)
        print("Podaj pierwszy koniec przedziału interpolacji: ")
        x1 = float(input())
        print("Podaj drugi koniec przedziału interpolacji: ")
        x2 = float(input())
        print("Podaj liczbę węzłów równoodległych")
        ileWezlow = int(input())

        if x2 > x1 and ileWezlow > 0:
            wykresInterpolacyjny(f, x1, x2, ileWezlow)


print("Interpolacja metodą Newtona dla węzłów równoodległych")

while 1:
    menu()
