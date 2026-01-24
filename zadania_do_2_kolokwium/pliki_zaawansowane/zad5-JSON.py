import json
from pydantic import BaseModel


def wczytaj_konfiguracje(sciezka_pliku: str) -> dict:
    try:
        with open(sciezka_pliku, "r", encoding="utf-8") as f:
            dane = json.load(f)
        return dane

    except FileNotFoundError:
        print("Błąd: plik nie istnieje")
        return {}

    except json.JSONDecodeError:
        print("Błąd: niepoprawny format JSON")
        return {}


konfiguracja = wczytaj_konfiguracje("konfiguracja.json")

print(konfiguracja)

print(konfiguracja["baza_danych"]["uzytkownik"])

moje_dane = {
    "imie": "Piotrek",
    "wiek": 21,
    "ulubiony_kolor": "żółty",
    "hobby": ["programowanie", "gry", "siłownia"]
}


def zapisz_jako_json(dane: dict | list, sciezka_pliku: str):
    try:
        with open(sciezka_pliku, "w", encoding="utf-8") as f:
            json.dump(dane, f, ensure_ascii=False, indent=4)

        print("Zapis do pliku json zakonczony sukcesem")

    except IOError:
        print("Blad: nie udalo sie zapisac pliku")


zapisz_jako_json(moje_dane, "dane.json")


class SpecyfikacjaModel(BaseModel):
    procesor: str
    ram_gb: int


class ProduktModel(BaseModel):
    nazwa_produktu: str
    id_produktu: str
    cena: float
    dostepny: bool
    tagi: list[str]
    specyfikacja: SpecyfikacjaModel


def wczytaj_i_waliduj_produkt(sciezka: str) -> ProduktModel | None:
    try:
        with open(sciezka, "r", encoding="utf-8") as f:
            dane = json.load(f)

        produkt = ProduktModel.parse_obj(dane)
        return produkt

    except FileNotFoundError:
        print("Błąd: plik nie istnieje")
        return None

    except json.JSONDecodeError:
        print("Błąd: niepoprawny format JSON")
        return None

    except ValidationError as e:
        print("Błąd walidacji danych:")
        print(e)
        return None


produkt = wczytaj_i_waliduj_produkt("produkt.json")

if produkt:
    print(produkt.nazwa_produktu)
    print(produkt.specyfikacja.procesor)
