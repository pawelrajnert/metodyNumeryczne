import math

from funkcje import funkcjaWagowa


def kwadraturaGaussaCzebyszewa(funkcja, ileWezlow):
    wynik = .0
    A = math.pi / (ileWezlow)
    # wzór według kalkulatora Wolfram (strona mathworld.wolfram)
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
    suma = (funkcja(a) * funkcjaWagowa(a)) + (funkcja(b) * funkcjaWagowa(b))

    for i in range(1, n):
        if i % 2 == 0:
            suma += 2 * funkcja(a + i * h) * funkcjaWagowa(a + i * h)
        else:
            suma += 4 * funkcja(a + i * h) * funkcjaWagowa(a + i * h)
    # według wzoru, jeśli rozważamy nieparzysty indeks to mamy wagę 2, a jeśli parzysty to wagę 4

    return (h * suma) / 3


def kwadraturaNewtonaCotesa(funckja, a, b, dokladnosc):
    n = 2
    wynikPoprzedni = wzorSimpsona(funckja, a, b, n)  # 1 wywołanie funkcji

    while 1:
        n += 2
        wynikKolejny = wzorSimpsona(funckja, a, b, n)

        if (wynikKolejny - wynikPoprzedni) < dokladnosc:  # jeśli spełniamy dokładność to kończymy działanie algorytmu
            return wynikKolejny

        wynikPoprzedni = wynikKolejny  # przygotowujemy wynik do kolejnej iteracji


def granicaNewtonaCotesa(funkcja, dokladnosc):
    wynik = 0

    a = 0
    b = 0.5
    while 1:
        # sprawdzamy wyniki dla granicy do +1
        wynikPrzedzial = kwadraturaNewtonaCotesa(funkcja, a, b, dokladnosc)

        # po każdej iteracji aktualizujemy wynik i wartość granicy przedziału
        wynik += wynikPrzedzial
        a = b
        b += (1 - b) / 2  # gdy mamy na poczatku np. 1/2 to robimy dzialanie: 1/2 + 1/2 * 1/2 = 3/4

        if abs(wynikPrzedzial) < dokladnosc:
            break

    a = -0.5
    b = 0
    while 1:
        # sprawdzamy wyniki dla granicy do -1
        wynikPrzedzial = kwadraturaNewtonaCotesa(funkcja, a, b, dokladnosc)

        # po każdej iteracji aktualizujemy wynik i wartość granicy przedziału
        wynik += wynikPrzedzial
        b = a
        a -= (1 - abs(a)) / 2  # gdy mamy na poczatku np. 1/2 to robimy dzialanie: -1/2 + (-1/2) * (-1/2) = -3/4

        if abs(wynikPrzedzial) < dokladnosc:
            break

    return wynik
