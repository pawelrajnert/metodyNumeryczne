import math

import numpy as np
from matplotlib import pyplot as plt


def horner(wspolczynniki, x):  # obliczamy wspolczynniki wielomianu schematem hornera
    wynik = 0

    for w in wspolczynniki:
        wynik = wynik * x + w

    return wynik


def wzorNewtona(wspolczynniki, wezly, x):
    wynik = wspolczynniki[0]
    pom = 1  # tutaj bedziemy trzymali wartosc z poprzedniego kroku, aby uproscic obliczenia

    for i in range(1, len(wspolczynniki)):
        pom *= (x - wezly[i - 1])
        wynik += wspolczynniki[i] * pom

    return wynik

# jak to działa?
# mamy wzór W(x) = y0 + f(x0:x1)(x-x0) + f(x0:x1:x2)((x-x0)(x-x1)) ...
# pom przechowuje nam te skladniki ktore potem sie powtarzaja

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


def testowa(x):
    return 1 / (1 + 25 * (x ** 2))


def wykresPoczatkowy(f, a, b):
    xDane = np.linspace(a, b)
    yDane = np.array([f(x) for x in xDane])
    plt.plot(xDane, yDane)
    plt.title("Funkcja początkowa")
    plt.show()


def wykresInterpolacyjny(f, a, b, ileWezlow):
    xDane = np.linspace(a, b)
    yDane = np.array([f(x) for x in xDane])  # funkcja podstawowa
    xWezly = np.linspace(a, b, ileWezlow)
    yWezly = np.array([f(x) for x in xWezly])  # funkcja interpolacyjna
    wspolczynniki = ilorazRoznicowy(xWezly, yWezly)
    interpolacja = np.array([wzorNewtona(wspolczynniki, xWezly, x) for x in xDane])

    plt.plot(xDane, yDane, label="Funkcja początkowa")
    plt.plot(xDane, interpolacja, label="Funkcja po interpolacji", linestyle="--")
    plt.scatter(xWezly, yWezly, color="red", label="Węzły interpolacji")
    plt.legend()
    plt.title("Wykres po interpolacji")
    plt.show()


def ilorazRoznicowy(x, y):
    pom = len(x)
    wynik = np.array(y).copy()
    for i in range(1, pom):
        wynik[i:] = (wynik[i:] - wynik[i - 1:-1]) / (x[i:] - x[:pom - i])
    return wynik

# jak to się oblicza? x = wezel, y = wartoscWezla = f(x)
# przechodzimy po kazdym elemencie- obliczamy iloraz różnicowy dla każdego węzła, aby na koniec móc narysować wykres
# wynik[i:] = bierzemy kazdy element z listy
# wynik[i - 1:-1] = bierzemy element o jeden mniejszy niz ten wyzej
# wezel[:pom - i] = dobieramy odpowiedni wezel
# dlaczego? bo "ogólnie mówiąc" wzór wygląda tak:
# (f(x) - f(x-1) / x - (x-1)
