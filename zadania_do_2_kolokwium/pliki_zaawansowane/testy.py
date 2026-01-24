import os

plik = open("przyklad.txt", "w")
plik.write("Witaj świecie!\n")
plik.write("To jest druga linia.\n")
plik.close()


# def podziel(a, b):
#     if b == 0:
#         raise ValueError("Nie można dzielić przez zero!")
#     return a / b
#
#
# try:
#     wynik = podziel(10, 1)
# except ValueError as e:
#     print("Błąd:", e)
#
# print(wynik)
#
# try:
#     x = int(input("Podaj liczbę: "))
#     print("Twoja liczba:", x)
# except ValueError:
#     print("To nie jest poprawna liczba!")


class MojPlik:
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __enter__(self):
        self.plik = open(self.nazwa, "w")
        return self.plik

    def __exit__(self, exc_type, exc_value, traceback):
        self.plik.close()
        if exc_type:
            print(f"Wystąpił błąd: {exc_value}")
        return True


with MojPlik("test.txt") as p:
    p.write("Hello z wlasnym menedzerem!")


def bezpieczny_zapis(nazwa, dane):
    temp = nazwa + ".tmp"
    with open(temp, "w") as f:
        f.write(dane)
    os.replace(temp, nazwa)

bezpieczny_zapis("przyklad.txt", "Nowe dane")


with open("log.txt", "r") as f:
    for linia in f:
        if "ERROR" in linia:
            print("Znaleziono błąd:", linia.strip())


class BezpieczneOtwieranie:
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __enter__(self):
        try:
            self.plik = open(self.nazwa, "r")
        except FileNotFoundError:
            print("Plik nie istnieje, tworzymy nowy")
            self.plik = open(self.nazwa, "w+")
        return self.plik

    def __exit__(self, exc_type, exc_value, traceback):
        self.plik.close()
        return True

with BezpieczneOtwieranie("nie_ma.txt") as f:
    f.write("Tworzymy plik jeśli nie istnieje")
