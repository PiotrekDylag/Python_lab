class Ekwipunek():
    def __init__(self, przedmioty=[]):
        self.przedmioty = przedmioty

    def dodaj_przedmiot(self, przedmiot):
        self.przedmioty.append(przedmiot)

    def pokaz_przedmioty(self):
        print(self.przedmioty)


class Gracz(Ekwipunek):
    liczba_graczy = 0

    def __init__(self, imie, hp):
        self.imie = imie
        self._hp = int(hp)
        self.ekwipunek = Ekwipunek()
        Gracz.liczba_graczy += 1

    def przedstaw_sie(self):
        return f"Gracz {self.imie} (HP: {self.hp}), liczba graczy {self.liczba_graczy}"

    def otrzymaj_obrazenia(self, ilosc):
        self.hp -= ilosc
        if self.hp < 0:
            self.hp = 0
        return f"otrzymano {ilosc} obrażeń"

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, nowa_wartosc):
        if nowa_wartosc < 0:
            self._hp = 0
        else:
            self._hp = nowa_wartosc

    @staticmethod
    def sprawdz_poprawnosc_imienia(imie):
        if not imie:
            return False
        return imie[0].isupper()

    def __eq__(self, other):
        if isinstance(other, Gracz):
            return self.imie == other.imie
        return False

    def __str__(self):
        return f"Gracz {self.imie} (HP: {self.hp})"

    def __repr__(self):
        return f"Gracz({self.imie} HP: {self.hp})"


class Wojownik(Gracz):
    def __init__(self, imie, hp, sila):
        super().__init__(imie, hp)
        self.sila = sila

    def przedstaw_sie(self):
        tekst = super().przedstaw_sie()
        return f"{tekst}, Sila: {self.sila}"

    def atak(self):
        return f"Wojownik {self.imie} zaatakował z siłą {self.sila}"

    @classmethod
    def stworz_berserkera(cls, imie):
        return cls(imie, 80, 40)

    def __add__(self, other):
        if not isinstance(other, Wojownik):
            return NotImplemented

        nowe_imie = f"{self.imie} i {other.imie}"
        nowe_hp = self.hp + other.hp
        nowa_sila = self.sila + other.sila

        return Wojownik(nowe_imie, nowe_hp, nowa_sila)


class Mag(Gracz):
    def __init__(self, imie, hp, mana):
        super().__init__(imie, hp)
        self.mana = mana

    def przedstaw_sie(self):
        tekst = super().przedstaw_sie()
        return f"{tekst}, Mana: {self.mana}"


gracz1 = Gracz("Przemek", 100)
gracz1.ekwipunek.dodaj_przedmiot("Miecz")
print(gracz1.sprawdz_poprawnosc_imienia("przemek"))



gracz2 = Gracz("Przemek", 120)
gracz2.hp = -100

print(gracz1==gracz2)

print(gracz1.przedstaw_sie())
print(gracz1.ekwipunek.pokaz_przedmioty())
print(gracz2.przedstaw_sie())

woj1 = Wojownik("Garen", 100, 59)
print(woj1.przedstaw_sie())
print(woj1.atak())

woj2 = Wojownik("Aatrox", 150, 99)

fuzja = woj1 + woj2

print(fuzja.przedstaw_sie())

mag1 = Mag("Syndra", 80, 150)
print(mag1.przedstaw_sie())

berserker = Wojownik.stworz_berserkera("Olaf")
print(berserker.przedstaw_sie())

print("\n\n")

druzyna = (gracz1, woj1, mag1)

for gamer in druzyna:
    print(gamer.przedstaw_sie())
