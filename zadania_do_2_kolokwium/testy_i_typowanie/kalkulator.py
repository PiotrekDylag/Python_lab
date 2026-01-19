def dodaj(a: float, b: float) -> float:
    return a + b


def dziel(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Nie można dzielić przez zero")
    return a / b
