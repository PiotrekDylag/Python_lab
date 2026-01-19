import functools
from functools import reduce

liczby = [5, 19, 4, 2, 6]

najwieksza = reduce(lambda a, b: a if a > b else b, liczby)
print(najwieksza)



VAT = 0.23
def print_receipt(data):
    total = 0
    print("---PARAGON---")
    for item in data:
        price_with_tax = item["cena_netto"] * (1 + VAT)
        total += price_with_tax
        print(f"{item['nazwa']}... {price_with_tax}")
    print("SUMA: " + str(total))


# Przykładowe dane wejściowe
produkty = [
    {"nazwa": "Mleko", "cena_netto": 3.50},
    {"nazwa": "Czekolada", "cena_netto": 5.20},
]

print_receipt(produkty)
