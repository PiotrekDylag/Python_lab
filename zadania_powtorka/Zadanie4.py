import Zadanie3

def sprawdz_typy(typ_argumentu):
    def dekorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, typ_argumentu):
                    print(f"Błąd: wszystkie argumenty muszą być typu {typ_argumentu.__name__}")
                    return None
            return func(*args, **kwargs)
        return wrapper
    return dekorator


# Testujemy na funkcji dodaj
@sprawdz_typy(int)
def dodaj(a, b):
    return a + b


# Testy
print(dodaj(2, 3))      # Poprawne → 5
print(dodaj(2, 3.5))    # Błąd → None
print(dodaj("x", 1))    # Błąd → None


print(Zadanie3.filtered)