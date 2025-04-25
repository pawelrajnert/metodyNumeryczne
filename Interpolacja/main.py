from metody import *


def menu():
    print("Funkcja do interpolacji:")
    print("1) funkcja liniowa")
    print("2) moduł z x ")
    print("3) wielomian ")
    print("4) funkcja trygonometryczna ")
    print("5) złożenie funkcji ")
    print("6) wczytanie danych o funkcji z pliku tekstowego ")
    # jesli dobrze rozumiem to jedna funkcja ma byc tez z pliku?
    # w sensie podaje sie punkty i tak sie zrobi funkcja (jest metoda w wykladzie)?

    menu = int(input("Wybierz opcję: "))
    wybranoMetode = True

    if menu == 1:
        print("Wybrano funkcję liniową.")
        print("Funkcja jest w postaci: ")
        print("2x + 6")
        wykresPoczatkowy(liniowa, -3, 3)

    elif menu == 2:
        print("Wybrano funkcję moduł z x.")
        print("Funkcja jest postaci: ")
        print("|x|")
        wykresPoczatkowy(modul, -3, 3)

    elif menu == 3:
        print("Wybrano wielomian.")
        print("Wielomian jest w postaci: ")
        print("-x^3 + x^2 + 3x - 4 ")
        wykresPoczatkowy(wielomian, -3, 3)

    elif menu == 4:
        print("Wybrano funkcję trygonometryczną.")
        print("Funkcja trygonometryczna jest postaci: ")
        print("2sin(x) + 3cos(x) - 2")
        wykresPoczatkowy(trygonometryczna, -math.pi, math.pi)

    elif menu == 5:
        print("Wybrano złożenie funkcji.")
        print("Funkcja złożona jest postaci:")
        print("5sin(x) - 3x^2 + 2^x - |x| + 4")
        wykresPoczatkowy(zlozenie, -math.pi, math.pi)

    elif menu == 6:
        print("Wybrano wczytanie funkcji z pliku tekstowego 'funkcja.txt'.")
        # do zrobienia
        #wykresPoczatkowy(f, -math.pi, math.pi)

    else:
        wybranoMetode = False
        print("Błąd! Nie wybrano metody!")

    if wybranoMetode:
        print("Podaj pierwszy koniec przedziału interpolacji: ")
        x1 = float(input())
        print("Podaj drugi koniec przedziału interpolacji: ")
        x2 = float(input())
        if x2 < x1:
            interpolacja()


print("Interpolacja metodą Newtona dla węzłów równoodległych")

while 1:
    menu()
