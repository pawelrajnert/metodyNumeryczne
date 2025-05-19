from dodatkoweFunkcje import *

# strona 26 z prezentacji- rekurencyjne tworzenie wielomianów Czebyszewa
def tworzenieWielomianowCzebyszewa(n, x): # n- stopień wielomianu, x- wartość zmiennej x
    if n == 0:
        return 1

    elif n == 1:
        return x

    T = [1, x]
    for i in range(2, n + 1):
        wielomian = (2 * x * T[i - 1] - T[i - 2])
        T.append(wielomian)
    return T[n]

