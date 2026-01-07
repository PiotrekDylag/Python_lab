lista_zamowien = [
    {"id": 1, "klient": "Anna", "kwota": 120.50},
    {"id": 2, "klient": "Jan", "kwota": 560.00},
    {"id": 3, "klient": "Anna", "kwota": 80.00}
]

def analizuj_zamowienia(zamowienia, prog_kwoty):
    suma = 0
    najdrozsze = None
    unikalni = set()

    if not zamowienia:
        return {
            "suma": suma,
            "najdrozsze": najdrozsze,
            "unikalni": unikalni,
            "ponad_prog": False
        }


    for klient in zamowienia:
        suma += klient["kwota"]

        if najdrozsze is None or klient["kwota"] > najdrozsze["kwota"]:
            najdrozsze = klient

        unikalni.add(klient["klient"])

    ponad_prog = suma > prog_kwoty

    return {
        "suma": suma,
        "najdrozsze": najdrozsze["id"],
        "unikalni": unikalni,
        "ponad_prog": ponad_prog
    }

print(analizuj_zamowienia(lista_zamowien, 400.00))