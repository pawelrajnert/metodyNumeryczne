from obliczenia import wartoscFunkcji, pochodnaFunkcji


def bisekcja(x1, x2, menu, warunekStopu):
    if wartoscFunkcji(x1, menu) * wartoscFunkcji(x2, menu) > 0:
        print("Wybrany przedział nie spełnia warunków dla metody bisekcji!")
        return
    iterations = 0
    while True:
        iterations = iterations + 1
        x0 = (x1 + x2) / 2
        f_x0 = wartoscFunkcji(x0, menu)
        if f_x0 == 0:
            return x0, iterations
        elif f_x0 * wartoscFunkcji(x2, menu) < 0:
            x1 = x0
        else:
            x2 = x0
        if (isinstance(warunekStopu, int) and iterations >= warunekStopu) or (
                isinstance(warunekStopu, float) and abs(x1 - x2) < warunekStopu):
            return x0, iterations


def styczne(x1, x2, menu, warunekStopu):
    if wartoscFunkcji(x1, menu) * wartoscFunkcji(x2, menu) > 0:
        print("Wybrany przedział nie spełnia warunków dla metody Newtona!")
        return
    iterations = 0
    x0 = (x1 + x2) / 2  # założenie wstępne - wyznaczamy punkt, od którego będziemy dążyć (w samym środku przedziału)
    while True:
        if iterations != 0: x0 = x_1
        iterations += 1
        f_x0 = wartoscFunkcji(x0, menu)
        df_x0 = pochodnaFunkcji(x0, menu)
        if df_x0 == 0:
            print("Pochodna wynosząca 0, metoda Newtona nie działą.")
            return
        x_1 = x0 - f_x0 / df_x0
        if (isinstance(warunekStopu, int) and iterations >= warunekStopu) or (
                isinstance(warunekStopu, float) and abs(x0 - x_1) < warunekStopu):
            return x_1, iterations
