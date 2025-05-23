from dodatkoweFunkcje import *
from funkcje import *
from aproksymacja import *


def menu():
    print("Wybierz wielomian do aproksymacji:")
    print("1) f(x) = sin(x-2)")
    print("2) f(x) = x^2 + 3")
    print("3) f(x) = x^3 + 7x^2 - 15")
    print("4) f(x) = 2^x - 2")
    print("5) f(x) = x + 6")
    print("6) f(x) = (e^x + 4sin(x^2) - 3x^2 + 12) / (1 + x ** 2)")
    print("7) f(x) = sin(e^x + 4x)")
    print("8) f(x) = |x|")
    menu = int(input("Wybierz opcję: "))
    funkcja = None

    if menu == 1:
        funkcja = sinMinus2
    elif menu == 2:
        funkcja = sim
    elif menu == 3:
        funkcja = wielomian
    elif menu == 4:
        funkcja = wykladnicza
    elif menu == 5:
        funkcja = liniowa
    elif menu == 6:
        funkcja = zlozenie
    elif menu == 7:
        funkcja = zlozenie2
    elif menu == 8:
        funkcja = modulX
    else:
        print("Błąd! Nie wybrano metody!")
        return

    print("Wybierz tryb pracy programu:")
    print("1) aproksymacja wielomianem wybranego stopnia")
    print("2) aproksymacja do osiągnięcia zadanej dokładności (błąd aproksymacji)")

    wybor = int(input("Podaj swój wybór: "))
    a = float(input("Podaj lewy koniec przedziału: "))
    b = float(input("Podaj prawy koniec przedziału: "))
    wezly = int(input("Podaj liczbę węzłów do rozwiązania całki metodą Gaussa-Czebyszewa: "))

    if wybor == 1:
        stopien = int(input("Podaj stopień wielomianu aproksymującego: "))
        wykres(funkcja, wspolczynnikA(funkcja, wezly, stopien), a, b)

    elif wybor == 2:
        blad = float(input("Wprowadź oczekiwaną wartość błędu: "))
        wykresBlad(funkcja, wezly, a, b, blad)


print("Program implementujący metodę aproksymacji opartą o wielomiany Czebyszewa")

while 1:
    menu()
