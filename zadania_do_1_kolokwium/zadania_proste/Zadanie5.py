produkty = [
    {"nazwa": "banan", "cena": 1.99},
    {"nazwa": "jajka", "cena": 2.39},
    {"nazwa": "mleko", "cena": 4.50},
]

sortowana = sorted(produkty, key=lambda x: x["cena"])
for p in sortowana:
    print(p["nazwa"], ":", p["cena"])

print("\n")
oceny = [2, 3, 5, 3, 4]
czy_zagrozenie = any(oceny) < 3
print(czy_zagrozenie)


