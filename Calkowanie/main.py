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
        print(kwadraturaGaussaCzebyszewa(tutorialPrzykladGC, 1))
        print(kwadraturaGaussaCzebyszewa(tutorialPrzykladGC, 2))
        print(kwadraturaGaussaCzebyszewa(tutorialPrzykladGC, 3))
        print(kwadraturaGaussaCzebyszewa(tutorialPrzykladGC, 4))
        print(kwadraturaGaussaCzebyszewa(tutorialPrzykladGC, 5))
        print(kwadraturaGaussaCzebyszewa(tutorialPrzykladGCv2, 1))
        print(kwadraturaGaussaCzebyszewa(tutorialPrzykladGCv2, 2))
        print(kwadraturaGaussaCzebyszewa(tutorialPrzykladGCv2, 3))
        print(kwadraturaGaussaCzebyszewa(tutorialPrzykladGCv2, 4))
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
