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

    menu = int(input("Wybierz opcję: "))
    wybranoMetode = True

    if menu == 1:
        funkcja = sinMinus2
        dokladnosc = float(input("Wprowadź dokładność obliczeń: "))
        print("Obliczenia dla kwadratury Newtona-Cotesa: ")
        print(granicaNewtonaCotesa(funkcja, dokladnosc))
        print("Obliczenia dla kwadratury Gaussa-Czebyszewa: ")
        for i in range(2, 6):
            print("Kwadratura Gaussa-Czebyszewa dla", i, "węzłów.")
            print(kwadraturaGaussaCzebyszewa(funkcja, i))

    elif menu == 2:
        funkcja = przyklad
        dokladnosc = float(input("Wprowadź dokładność obliczeń: "))
        print("Obliczenia dla kwadratury Newtona-Cotesa: ")
        print(granicaNewtonaCotesa(funkcja, dokladnosc))
        print("Obliczenia dla kwadratury Gaussa-Czebyszewa: ")
        for i in range(2, 6):
            print("Kwadratura Gaussa-Czebyszewa dla", i, "węzłów.")
            print(kwadraturaGaussaCzebyszewa(funkcja, i))

    elif menu == 3:
        funkcja = sim
        dokladnosc = float(input("Wprowadź dokładność obliczeń: "))
        print("Obliczenia dla kwadratury Newtona-Cotesa: ")
        print(granicaNewtonaCotesa(funkcja, dokladnosc))
        print("Obliczenia dla kwadratury Gaussa-Czebyszewa: ")
        for i in range(2, 6):
            print("Kwadratura Gaussa-Czebyszewa dla", i, "węzłów.")
            print(kwadraturaGaussaCzebyszewa(funkcja, i))

    elif menu == 4:
        funkcja = sim
        dokladnosc = float(input("Wprowadź dokładność obliczeń: "))
        print("Obliczenia dla kwadratury Newtona-Cotesa: ")
        print(granicaNewtonaCotesa(funkcja, dokladnosc))
        print("Obliczenia dla kwadratury Gaussa-Czebyszewa: ")
        for i in range(2, 6):
            print("Kwadratura Gaussa-Czebyszewa dla", i, "węzłów.")
            print(kwadraturaGaussaCzebyszewa(funkcja, i))

    elif menu == 5:
        funkcja = wykladnicza
        dokladnosc = float(input("Wprowadź dokładność obliczeń: "))
        print("Obliczenia dla kwadratury Newtona-Cotesa: ")
        print(granicaNewtonaCotesa(funkcja, dokladnosc))
        print("Obliczenia dla kwadratury Gaussa-Czebyszewa: ")
        for i in range(2, 6):
            print("Kwadratura Gaussa-Czebyszewa dla", i, "węzłów.")
            print(kwadraturaGaussaCzebyszewa(funkcja, i))

    elif menu == 6:
        funkcja = liniowa
        dokladnosc = float(input("Wprowadź dokładność obliczeń: "))
        print("Obliczenia dla kwadratury Newtona-Cotesa: ")
        print(granicaNewtonaCotesa(funkcja, dokladnosc))
        print("Obliczenia dla kwadratury Gaussa-Czebyszewa: ")
        for i in range(2, 6):
            print("Kwadratura Gaussa-Czebyszewa dla", i, "węzłów.")
            print(kwadraturaGaussaCzebyszewa(funkcja, i))

    else:
        wybranoMetode = False
        print("Błąd! Nie wybrano metody!")


print("Program implementujący dwie metody całkowania numerycznego:")
print("* złożoną kwadraturę Newtona-Cotesa na trzech węzłach")
print("* kwadraturę Gaussa-Czebyszewa (dla 2, 3, 4 lub 5 węzłów)\n")

while 1:
    menu()
