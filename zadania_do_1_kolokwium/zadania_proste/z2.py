def analizujOceny(uczniowie):
    suma = 0
    najlepszy = None
    unikalne = set()

    for uczen in uczniowie:
        ocena = uczen["ocena"]

        suma += ocena
        unikalne.add(ocena)

        if najlepszy is None or ocena>najlepszy["ocena"]:
            najlepszy = uczen

    srednia = suma / len(uczniowie)

    return {
        "srednia": srednia,
        "najlepszy_student": najlepszy,
        "unikalne_oceny": unikalne
    }


uczniowie = [
    {"imie": "Piotr", "ocena": 2},
    {"imie": "Aneta", "ocena": 3},
    {"imie": "Adrian", "ocena": 3},
    {"imie": "Maciek", "ocena": 4}
]

wynik = analizujOceny(uczniowie)
print(wynik)