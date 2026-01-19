def znajdz_wartosc(dane, szukany_klucz):
    for klucz, wartosc in dane.items():
        if klucz == szukany_klucz:
            return wartosc

        if isinstance(wartosc, dict):
            wynik_z_glebi = znajdz_wartosc(wartosc, szukany_klucz)

            if wynik_z_glebi is not None:
                return wynik_z_glebi

    return None


konfiguracja = {
    "uzytkownik": "admin",
    "baza_danych": {
        "host": "localhost",
        "port": 5432,
        "credentials": {
            "user": "db_user",
            "password": "secret_password"
        },
    }
}
haslo = znajdz_wartosc(konfiguracja, "password")
print(f"Znalezione hasło: {haslo}")

