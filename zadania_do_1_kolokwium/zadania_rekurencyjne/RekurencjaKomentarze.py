komentarze = {
    "id": 1,
    "autor": "admin",
    "lajki": 5,
    "odpowiedzi": [
        {
            "id": 2,
            "autor": "user1",
            "lajki": 3,
            "odpowiedzi": []
        },
        {
            "id": 3,
            "autor": "user2",
            "lajki": 10,
            "odpowiedzi": [
                {
                    "id": 4,
                    "autor": "user1",
                    "lajki": 2,
                    "odpowiedzi": []
                }
            ]
        }
    ]
}

def analizuj_komentarze(komentarz):
    liczba_komentarzy = 1
    suma_lajkow = komentarz["lajki"]
    unikalni = set([komentarz["autor"]])
    najlepszy = {"id": komentarz["id"], "lajki": komentarz["lajki"]}

    for element in komentarz["odpowiedzi"]:
        wynik = analizuj_komentarze(element)
        liczba_komentarzy += wynik["liczba_komentarzy"]
        suma_lajkow += wynik["suma_lajkow"]
        unikalni.update(wynik["unikalni"])

        if wynik["najlepszy"]["lajki"] > najlepszy["lajki"]:
            najlepszy = wynik["najlepszy"]


    return {
        "liczba_komentarzy": liczba_komentarzy,
        "suma_lajkow": suma_lajkow,
        "unikalni": unikalni,
        "najlepszy": najlepszy
    }

print(analizuj_komentarze(komentarze))