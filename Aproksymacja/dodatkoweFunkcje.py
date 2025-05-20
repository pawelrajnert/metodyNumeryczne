import numpy as np
import matplotlib.pyplot as plt

from aproksymacja import *

# metoda Gaussa-Czebyszewa rozwiązywania całek z zadania 4
def kwadraturaGaussaCzebyszewa(funkcja, ileWezlow):
    wynik = .0
    A = math.pi / ileWezlow

    if ileWezlow in (2, 3, 4, 5):
        for i in range(1, ileWezlow + 1):
            xn = math.cos(((2 * i - 1) * math.pi) / (2 * ileWezlow))
            wynik += A * funkcja(xn)
    else:
        print("Wprowadzono niepoprawną ilość węzłów! Możliwa ilość do wyboru to: 2, 3, 4 lub 5.")
        return None

    return wynik


# schemat Hornera, wykorzystywany do obliczania współczynników wielomianu zgodnie z poleceniem
def horner(wspolczynniki, x):
    wynik = 0

    for w in wspolczynniki:
        wynik = wynik * x + w

    return wynik


# ostatni slajd prezentacji- przekształcenie dowolnego przedziału [a, b] na przedział [-1, 1]
def transformacja(a, b, x):
    return (2 * x - a - b) / (b - a)


def wykres(f, wspolczynnikiA, a, b):
    xDane = np.linspace(a, b)
    yDane = np.array([f(x) for x in xDane])
    yPoAproksymacji = [aproksymacja(x, wspolczynnikiA) for x in xDane]
    plt.plot(xDane, yDane, label="Funkcja początkowa", color="black")
    plt.plot(xDane,yPoAproksymacji,label="Funkcja aproksymowana", color="red")
    plt.title("Wykres funkcji podstawowej oraz aproksymacji funkcji")
    plt.legend()
    plt.show()
