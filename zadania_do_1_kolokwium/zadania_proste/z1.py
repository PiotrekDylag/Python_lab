pracownicy = [
    {"imie": "Anna", "stanowisko": "Specjalista", "pensja": 4500},
    {"imie": "Piotr", "stanowisko": "Manager", "pensja": 8000},
    {"imie": "Zofia", "stanowisko": "Specjalista", "pensja": 5200},
]

lista_plac = [p["pensja"] for p in pracownicy if p["stanowisko"] == "Specjalista"]

print(lista_plac)

zduplikowane_dane = [
    {'id': 1, 'imie': 'Anna'},
    {'id': 2, 'imie': 'Piotr'},
    {'id': 1, 'imie': 'Anna'},  # Duplikat
    {'id': 3, 'imie': 'Zofia'},
]

widziane_id = set()

unikalne_id = [
    (i["id"], i["imie"])
    for i in zduplikowane_dane
    if i["id"] not in widziane_id and not widziane_id.add(i["id"])
]

print(widziane_id)
print(unikalne_id)
