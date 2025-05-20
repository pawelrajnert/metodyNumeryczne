import math


def przyklad(x):
    return (1 - x ** 2) ** (3 / 2) * math.cos(x)


def sinMinus2(x):
    return math.sin(x - 2)


def sim(x):
    return (x ** 2 + 3)


def wielomian(x):
    return (x ** 3) + (7 * x ** 2) - 15


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
