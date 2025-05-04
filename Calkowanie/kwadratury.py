import math


def kwadraturaGaussaCzebyszewa(funkcja, ileWezlow):
    wynik = .0
    A = math.pi / (ileWezlow + 1)
    # według prezentacji wykładowej:
    # A = pi / n + 1
    # xn = cos((2i + 1 * pi) / 2n + 2)
    # całka = suma od i = 0 do n: A * f(xi)

    for i in range(0, ileWezlow + 1):
        xn = math.cos(((2 * i + 1) * math.pi) / (2 * ileWezlow + 2))
        wynik += A * funkcja(xn)

    return wynik
