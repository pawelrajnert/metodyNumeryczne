import math

import numpy as np
from matplotlib import pyplot as plt


def horner(wspolczynniki, x):  # dla wielomianów interpolowanych
    wynik = 0

    for w in wspolczynniki:
        wynik = wynik * x + w

    print("debug: ", wynik)
    return wynik


def pozostaleWyniki(wspolczynniki, wezly, x):  # dla wielomianow interpolacyjnych
    wynik = 0

    for w in wspolczynniki:
        print("aa")

    return wynik


def liniowa(x):
    return 2 * x + 6


def modul(x):
    return abs(x)


def wielomian(x):
    wspolczynniki = [-1, 1, 3, -4]
    return horner(wspolczynniki, x)


def trygonometryczna(x):
    return 2 * math.sin(x) + 3 * math.cos(x) - 2


def zlozenie(x):
    return 5 * math.sin(x) - 3 * (x ** 2) + (2 ** x) - abs(x) + 4


def zewnetrzna(x):
    print("do zrobienia")


def wykresPoczatkowy(f, a, b):
    xDane = np.linspace(a, b)
    yDane = np.array([f(x) for x in xDane])
    plt.plot(xDane, yDane, label="Funkcja początkowa")
    plt.title("Początkowy wykres funkcji")
    plt.legend()
    plt.show()


def wykresInterpolacyjny(f, a, b): # do zrobienia
    xDane = np.linspace(a, b)
    yDane = np.array([f(x) for x in xDane])
    plt.plot(xDane, yDane, label="Funkcja po interpolacji")
    plt.title("Wykres funkcji po po interpolacji")
    plt.legend()
    plt.show()


def interpolacja():
    print("do zrobienia")

def zrobWezly():
    print("do zrobienia")
