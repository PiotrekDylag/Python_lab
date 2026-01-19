pracownicy = [
    {"imie": "Anna", "nazwisko": "Kowalska", "stanowisko": "Programista", "pensja": 8000},
    {"imie": "Piotr", "nazwisko": "Nowak", "stanowisko": "Programista", "pensja": 7000},
    {"imie": "Katarzyna", "nazwisko": "Wiśniewska", "stanowisko": "Projektant", "pensja": 7500},
    {"imie": "Marek", "nazwisko": "Lewandowski", "stanowisko": "Tester", "pensja": 6500},
    {"imie": "Ewa", "nazwisko": "Zielińska", "stanowisko": "Kierownik", "pensja": 10000}
]
suma = 0
for p in pracownicy:
    suma += p["pensja"]
srednia = suma / len(pracownicy)
print(srednia)

sortowanaPensje = sorted(pracownicy, key=lambda k: k["pensja"], reverse=True)
print(sortowanaPensje[0]["nazwisko"], sortowanaPensje[0]["imie"])

for st in pracownicy:
    if st["stanowisko"] == "Programista":
        print(st["imie"], st["nazwisko"], st["stanowisko"])




