import math

from dodatkoweFunkcje import horner


def przyklad(x):
    return (1 - x ** 2) ** (3 / 2) * math.cos(x)


def sinMinus2(x):
    return math.sin(x - 2)


def sim(x):
    wspolczynniki = [1, 3]
    return horner(wspolczynniki, x)


def wielomian(x):
    wspolczynniki = [1, 7, 0, -15]
    return horner(wspolczynniki, x)


def wykladnicza(x):
    return (2 ** x) - 2


def liniowa(x):
    return x + 6


def zlozenie(x):
    return (math.e ** x + 4 * math.sin(x ** 2) - 3 * x ** 2 + 12) / (1 + x ** 2)


def zlozenie2(x):
    return math.sin(math.e ** x + 4 * x)


def funkcjaWagowa(x):
    return 1 / math.sqrt(1 - x ** 2)


def modulX(x):
    return abs(x)
