import csv

def wczytaj_pracownikow(sciezka_pliku: str) -> list:
    pracownicy = []

    try:
        with open(sciezka_pliku, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for wiersz in reader:
                try:
                    wiersz["pensja"] = int(wiersz["pensja"])
                    pracownicy.append(wiersz)
                except ValueError:
                    print(f"Ostrzeżenie: pomijam wiersz {wiersz}")

    except FileNotFoundError:
        print("Błąd: plik nie istnieje")

    return pracownicy

wynik = wczytaj_pracownikow("pracownicy.csv")

print("Poprawnie wczytani pracownicy:")
for p in wynik:
    print(p)
