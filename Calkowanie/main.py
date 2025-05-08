from kwadratury import *
from funkcje import *


def menu():
    print("Wybierz wielomian Czebyszewa do całkowania:")
    print("1) podstawowy przyklad f(x) = 1")
    print("2) testowy przykład f(x) = (1 - x^2)^3/2 ")

    menu = int(input("Wybierz opcję: "))
    wybranoMetode = True

    if menu == 1:
        wezly = int(input("Wprowadź ilość węzłów: "))
        print(kwadraturaGaussaCzebyszewa(podstawowa, wezly))

    elif menu == 2:
        print(granicaNewtonaCotesa(testowa, 1, 1, 1))  # tu do sprawdzenia
        print(kwadraturaGaussaCzebyszewa(testowa, 2))
        print(kwadraturaGaussaCzebyszewa(testowa, 3))
        print(kwadraturaGaussaCzebyszewa(testowa, 4))
        print(kwadraturaGaussaCzebyszewa(testowa, 5))
        wezly = int(input("Wprowadź ilość węzłów: "))
        print(kwadraturaGaussaCzebyszewa(tutorialPrzykladGC, wezly))


    else:
        wybranoMetode = False
        print("Błąd! Nie wybrano metody!")

    if wybranoMetode:
        print("a")


print("Program implementujący dwie metody całkowania numerycznego:")
print("* złożoną kwadraturę Newtona-Cotesa na trzech węzłach")
print("* kwadraturę Gaussa-Czebyszewa (dla 2, 3, 4 lub 5 węzłów)\n")

while 1:
    menu()
