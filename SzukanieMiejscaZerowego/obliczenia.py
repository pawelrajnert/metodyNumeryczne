import math
import numpy as np


def wartoscFunkcji(x, typ):
    wynik = 0
    wsp = wspolczynnikiFunkcji(typ)
    if typ == 1:  # -x^3 + x^2 + 3x - 4
        for i in wsp:
            wynik = wynik * x + i
    elif typ == 2:  # 2 sin(x) + 3 cos(x) - 2
        wynik = wsp[0] * np.sin(x) + wsp[1] * np.cos(x) + wsp[2]
    elif typ == 3:  # 2^x - 2
        wynik = wsp[0] ** x + wsp[1]
    elif typ == 4:  # 5 sin(x) - 3x^2 + 2^x
        wynik = wsp[0] * np.sin(x) + wsp[1] * x * x + wsp[2] ** x
    return wynik


def pochodnaFunkcji(x, typ):
    wynik = 0
    wsp = wspolczynnikiFunkcji(typ)
    if typ == 1:
        wynik = 3 * wsp[0] * x * x + 2 * wsp[1] * x + wsp[2]
    elif typ == 2:
        wynik = wsp[0] * math.cos(x) - wsp[1] * math.sin(x)
    elif typ == 3:
        wynik = math.log(wsp[0]) * wsp[0] ** x
    elif typ == 4:
        wynik = wsp[0] * math.cos(x) + wsp[1] * 2 * x + math.log(wsp[2]) * wsp[2] ** x
    return wynik


def wspolczynnikiFunkcji(menu):
    if menu == 1:
        wspolczynniki = [-1, 1, 3, -4]
    elif menu == 2:
        wspolczynniki = [2, 3, -2]
    elif menu == 3:
        wspolczynniki = [2, -2]
    elif menu == 4:
        wspolczynniki = [5, -3, 2]
    return wspolczynniki
