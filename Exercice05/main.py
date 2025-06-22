def add(a, b):
    """
    Additionne deux nombres.
    nombre a et b
    Retourne:
    La somme de a et b.
    """
    return a + b


def subtraction(a, b):
    """
    Soustrait le premier nombre avec le deuxieme.
    nombre a et b
    Retourne:
    nombre : La différence entre a et b.
    """
    return a - b


if __name__ == '__main__':
    test = add(1, 2)
    print(test)

    print(subtraction(10, 4))

