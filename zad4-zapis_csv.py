sprzedaz = [
    {"produkt": "Laptop", "sprzedana_ilosc": 5, "przychody": 25000},
    {"produkt": "Monitor", "sprzedana_ilosc": 8, "przychody": 6400},
    {"produkt": "Mysz", "sprzedana_ilosc": 20, "przychody": 2000},
]

import csv


def zapisz_raport_sprzedazy(sciezka_pliku: str, dane: list):
    # c.
    if not dane:
        print("Brak danych do zapisania.")
        return

    # d.
    naglowki = dane[0].keys()

    # e. + f.
    with open(sciezka_pliku, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=naglowki)
        writer.writeheader()
        writer.writerows(dane)

    print("Raport sprzedaży zapisany poprawnie.")

zapisz_raport_sprzedazy("raport.csv", sprzedaz)
