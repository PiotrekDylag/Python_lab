import time

def czas(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = func(*args, **kwargs)
        end = time.time()
        print(f"Czas wykonania: {end - start:.6f} s")
        return wynik
    return wrapper


@czas
def pokaz_dane(**dane):
    print(f"Otrzymano słownik: {dane}")
    for k, w in dane.items():
        print(f"- {k}: {w}")


pokaz_dane(imie="Jan", wiek=40, miasto="Warszawa")
