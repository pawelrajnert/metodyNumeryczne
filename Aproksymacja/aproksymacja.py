import math

import numpy as np

przekazStopien = 0

# strona 26 z prezentacji- rekurencyjne tworzenie wielomianów Czebyszewa
# jest to tworzenie Tk do wzoru, a dokladnie jego wartosci
def tworzenieWielomianowCzebyszewa(stopien, x):  # stopien- stopień wielomianu, x- wartość zmiennej x
    if stopien == 0:
        return [1]

    elif stopien == 1:
        return [1, x]

    T = [1, x]
    for i in range(2, stopien + 1):
        wielomian = (2 * x * T[i - 1] - T[i - 2])
        T.append(wielomian)
    return T


# obliczamy współczynnik A, potrzebujemy do tego obliczyc calke za pomoca naszej kwadratury + wynik z funkcji T
def wspolczynnikA(funkcja, wezly, stopien):
    from dodatkoweFunkcje import kwadraturaGaussaCzebyszewa
    wspolczynnikiA = []

    for i in range(0, stopien + 1):
        def mnozenieFunkcji(x, pom=i):
            T = tworzenieWielomianowCzebyszewa(stopien, x)
            return funkcja(x) * T[pom]

        wynik = 2 / math.pi * kwadraturaGaussaCzebyszewa(mnozenieFunkcji, wezly)

        wspolczynnikiA.append(wynik)

    return wspolczynnikiA

# wykonujemy aproksymacje wielomianem (dla podanego stopnia)
def aproksymacja(x, wspolczynnikA):
    T = tworzenieWielomianowCzebyszewa(len(wspolczynnikA) - 1, x)
    wynik = wspolczynnikA[0] / 2 * T[0]

    for i in range(1, len(wspolczynnikA)):
        wynik += wspolczynnikA[i] * T[i]

    return wynik

# wykonujemy aproksymacje dla zadanej dokladnosci- dopóki nie osiągniemy oczekiwanego wyniku wykonujemy pętlę (ale mamy limit 30 stopnia wielomianu)
def aproksymacjaBledem(funkcja, x, wezly, blad, a, b):
    obecnyStopien = 1  # zgodnie z poleceniem, w przypadku wersji iteracyjnej zaczynamy od stopnia 1 i sprawdzamy dalej do osiągnięcia dokładności
    A = wspolczynnikA(funkcja, wezly, obecnyStopien)
    porownajBlad = bladAproksymacji(funkcja, A, a, b)

    # sprawdzamy warunek do osiągnięcia oczekiwanej dokładności lub w przypadku niepowodzenia ograniczamy stopień wielomianu do 30
    while porownajBlad > blad and obecnyStopien < 30:
        obecnyStopien += 1
        A = wspolczynnikA(funkcja, wezly, obecnyStopien)
        porownajBlad = bladAproksymacji(funkcja, A, a, b)

    global przekazStopien
    przekazStopien = obecnyStopien
    from dodatkoweFunkcje import transformacja
    xPrzedzial = transformacja(a, b, x)
    wynik = aproksymacja(xPrzedzial, A)
    return wynik


# obliczamy błąd aproksymacji zgodnie z prezentacją
def bladAproksymacji(funkcja, wspolczynnikiA, a, b):
    blad = .0
    xDane = np.linspace(a, b)
    from dodatkoweFunkcje import transformacja

    for x in xDane:
        przedzial = transformacja(a, b, x)
        F = funkcja(x)
        A = aproksymacja(przedzial, wspolczynnikiA)
        blad += (F - A) ** 2

    blad = math.sqrt(blad / 50)  # bo 50 to defaultowa liczba punktów
    return blad

def podajStopien():
    return przekazStopien