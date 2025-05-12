from kwadratury import *
from funkcje import *


def menu():
    print("Wybierz wielomian Czebyszewa do całkowania:")
    print("1) f(x) = sin(x-2)")
    print("2) f(x) = (1 - x^2)^3/2 * cos(x)")
    print("3) f(x) = x^2 + 3")
    print("4) f(x) = x^3 + 7x^2 - 15")
    print("5) f(x) = 2^x - 2")
    print("6) f(x) = x + 6")
    print("7) f(x) = (e^x + 4sin(x^2) - 3x^2 + 12) / (1 + x ** 2)")
    print("8) f(x) = sin(e^x + 4x)")
    menu = int(input("Wybierz opcję: "))
    funkcja = None

    if menu == 1:
        funkcja = sinMinus2
    elif menu == 2:
        funkcja = przyklad
    elif menu == 3:
        funkcja = sim
    elif menu == 4:
        funkcja = wielomian
    elif menu == 5:
        funkcja = wykladnicza
    elif menu == 6:
        funkcja = liniowa
    elif menu == 7:
        funkcja = zlozenie
    elif menu == 8:
        funkcja = zlozenie2
    else:
        print("Błąd! Nie wybrano metody!")
        return
    dokladnosc = float(input("Wprowadź dokładność obliczeń: "))
    print("Obliczenia dla kwadratury Newtona-Cotesa: ")
    print(granicaNewtonaCotesa(funkcja, dokladnosc))
    print("Obliczenia dla kwadratury Gaussa-Czebyszewa: ")
    for i in range(2, 6):
        print("Kwadratura Gaussa-Czebyszewa dla", i, "węzłów.")
        print(kwadraturaGaussaCzebyszewa(funkcja, i))



print("Program implementujący dwie metody całkowania numerycznego:")
print("* złożoną kwadraturę Newtona-Cotesa na trzech węzłach")
print("* kwadraturę Gaussa-Czebyszewa (dla 2, 3, 4 lub 5 węzłów)\n")

while 1:
    menu()
