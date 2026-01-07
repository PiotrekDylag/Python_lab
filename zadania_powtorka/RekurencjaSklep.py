sklep = {
    "nazwa": "Sklep",
    "produkty": [
        {
            "typ": "produkt",
            "cena": 120
        },
        {
            "typ": "kategoria",
            "produkty": [
                {
                    "typ": "produkt",
                    "cena": 80
                },
                {
                    "typ": "kategoria",
                    "produkty": [
                        {
                            "typ": "produkt",
                            "cena": 200
                        }
                    ]
                }
            ]
        },
        {
            "typ": "produkt",
            "cena": 60
        }
    ]
}

def oblicz_wartosc(kategoria):
    suma = 0

    for element in kategoria["produkty"]:
        if element["typ"] == "produkt":
            suma += element["cena"]
        else:
            suma += oblicz_wartosc(element)

    return suma

print(oblicz_wartosc(sklep))