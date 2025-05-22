import math
import numpy as np
import matplotlib.pyplot as plt

from aproksymacja import wspolczynnikA


# metoda Gaussa-Czebyszewa rozwiązywania całek z zadania 4
def kwadraturaGaussaCzebyszewa(funkcja, ileWezlow):
    wynik = .0
    A = math.pi / ileWezlow

    for i in range(1, ileWezlow + 1):
        xn = math.cos(((2 * i - 1) * math.pi) / (2 * ileWezlow))
        wynik += A * funkcja(xn)

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


def wykres(funkcja, wspolczynnikiA, a, b):
    from aproksymacja import aproksymacja, bladAproksymacji

    xDane = np.linspace(a, b)
    yDane = np.array([funkcja(x) for x in xDane])
    yPoAproksymacji = [aproksymacja(transformacja(a, b, x), wspolczynnikiA) for x in xDane]

    print("Błąd aproksymacji: ", bladAproksymacji(funkcja, wspolczynnikiA, a, b))
    plt.plot(xDane, yDane, label="Funkcja początkowa", color="black")
    plt.plot(xDane, yPoAproksymacji, label="Funkcja po aproksymacji", color="red")
    plt.legend()
    plt.show()


def wykresBlad(funkcja, wezly, a, b, blad):
    from aproksymacja import aproksymacjaBledem, podajStopien, bladAproksymacji, wspolczynnikA

    xDane = np.linspace(a, b)
    yDane = np.array([funkcja(x) for x in xDane])
    yPoAproksymacji = [aproksymacjaBledem(funkcja, x, wezly, blad, a, b) for x in xDane]

    pom = podajStopien()
    if (pom != 30):
        print("Znaleziono rozwiązanie o zadanej dokładności, z wykorzystaniem wielomianu stopnia:", pom)

    else:
        print("Nie znaleziono rozwiązania o zadanej dokładności, wynik dla wielomianu stopnia:", pom)

    A = wspolczynnikA(funkcja, wezly, pom)
    print("Błąd aproksymacji: ", bladAproksymacji(funkcja, A, a, b))
    plt.plot(xDane, yDane, label="Funkcja początkowa", color="black")
    plt.plot(xDane, yPoAproksymacji, label="Funkcja po aproksymacji", color="red")
    plt.legend()
    plt.show()
