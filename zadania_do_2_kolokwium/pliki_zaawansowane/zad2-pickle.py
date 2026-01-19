import pickle  # a.

# b.
class StanGry:
    def __init__(self, nazwa_gracza: str, punkty: int, ekwipunek: list):
        self.nazwa_gracza = nazwa_gracza
        self.punkty = punkty
        self.ekwipunek = ekwipunek

    def __repr__(self):
        return (f"StanGry(nazwa_gracza='{self.nazwa_gracza}', "
                f"punkty={self.punkty}, "
                f"ekwipunek={self.ekwipunek})")


# c.
stan = StanGry(
    nazwa_gracza="Piotrek",
    punkty=420,
    ekwipunek=["miecz", "tarcza", "mikstura"]
)

# d. + e. zapis do pliku
with open("stan_gry.pkl", "wb") as f:
    pickle.dump(stan, f)

print("Stan gry zapisany do pliku.")

# f. + g. odczyt z pliku
with open("stan_gry.pkl", "rb") as f:
    wczytany_stan = pickle.load(f)

# h.
print("Wczytany stan gry:")
print(wczytany_stan)
print("Typ obiektu:", type(wczytany_stan))
