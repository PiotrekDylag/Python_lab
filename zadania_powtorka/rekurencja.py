def splaszcz_liste(elementy):
    wyniki = []
    for elem in elementy:
        if isinstance(elem, list):
            wyniki.extend(splaszcz_liste(elem))
        else:
            wyniki.append(elem)

    return wyniki


zagniezdzona_lista = [1, [2, 3], 4, [5, [6, 7]]]

print(splaszcz_liste(zagniezdzona_lista))