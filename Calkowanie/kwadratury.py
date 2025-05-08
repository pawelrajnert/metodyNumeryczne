import math


def kwadraturaGaussaCzebyszewa(funkcja, ileWezlow):
    wynik = .0
    A = math.pi / (ileWezlow)
    # wzór według kalkulatora Wolfram
    # w przypadku implementacji wzoru z prezentacji wykładowej, wyniki dla węzłów są przesunięte o 1
    if ileWezlow in (2, 3, 4, 5):
        for i in range(1, ileWezlow + 1):
            xn = math.cos(((2 * i - 1) * math.pi) / (2 * ileWezlow))
            wynik += A * funkcja(xn)
    else:
        print("Wprowadzono niepoprawną ilość węzłów! Możliwa ilość do wyboru to: 2, 3, 4 lub 5.")
        return None

    return wynik


def wzorSimpsona(funkcja, a, b, n):
    if n % 2 == 1 or n == 0:
        print("Niepoprawna wartość podprzedziałów! Należy wprowadzić liczbę parzystą.")
        return None

    h = (b - a) / n  # dzielimy przedział na równe części
    suma = funkcja(a) + funkcja(b)

    for i in range(1, n):
        if i % 2 == 0:
            suma += 2 * funkcja(a + i * h)
        else:
            suma += 4 * funkcja(a + i * h)
    # według wzoru, jeśli rozważamy nieparzysty indeks to mamy wagę 2, a jeśli parzysty to wagę 4

    return (h * suma) / 3


# wariant dla całki z określonym przedziałem skończonym
def kwadraturaNewtonaCotesa(funckja, a, b, dokladnosc):
    n = 2
    wynikPoprzedni = wzorSimpsona(funckja, a, b, n)  # 1 wywołanie funkcji

    while 1:
        n += 2
        wynikKolejny = wzorSimpsona(funckja, a, b, n)

        if (wynikKolejny - wynikPoprzedni) < dokladnosc:  # jeśli spełniamy dokładność to kończymy działanie algorytmu
            return wynikKolejny

        wynikPoprzedni = wynikKolejny  # przygotowujemy wynik do kolejnej iteracji


# wariant dla całki z granicą niewłaściwą
def granicaNewtonaCotesa(funkcja, a, delta, dokladnosc):
    if delta < 0:  # warunek w poleceniu zadania
        print("Niepoprawna wartość delty!")
        return None

    if a < 0:  # sprawdzenie podobnie jak w przypadku delty
        print("Niepoprawna wartość granicy przedziału!")
        return None

    wynik = kwadraturaNewtonaCotesa(funkcja, 0, a, dokladnosc)

    while 1:
        # sprawdzamy wynik na przedziale (a, a + delta)
        wynikDelta = kwadraturaNewtonaCotesa(funkcja, a, a + delta, dokladnosc)

        if abs(wynikDelta) < dokladnosc:
            return wynik

        # po każdej iteracji aktualizujemy wynik i wartość granicy przedziału
        wynik += wynikDelta
        a += delta

# do zweryfikowania
# Przy obliczaniu kwadratur Newtona-Cotesa trzeba więc dodać funkcję wagową.
# W przypadku wariantów 1-3 w kwadraturze Newtona-Cotesa konieczne jest dodatkowo obliczanie granicy.
# Bez tego wyniki uzyskane obiema metodami nie byłyby porównywalne. chyba to co mamy w funkcji granica wystarcza
