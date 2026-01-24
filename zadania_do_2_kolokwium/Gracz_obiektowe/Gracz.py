from dataclasses import dataclass
from functools import total_ordering
from abc import ABC, abstractmethod


class BrakPunktowZdrowiaError(Exception):
    pass


class Bohater(ABC):
    @abstractmethod
    def atakuj(self) -> str:
        pass

    @abstractmethod
    def opis(self) -> str:
        pass


class StrategiaAtaku(ABC):
    @abstractmethod
    def atakuj(self) -> str:
        pass


class AtakMieczem(StrategiaAtaku):
    def atakuj(self) -> str:
        return "Cios mieczem *CIACH*"


class AtakKulaOgnia(StrategiaAtaku):
    def atakuj(self) -> str:
        return "Rzut kula ognia *BACH*"


class NieujemnaLiczba:
    def __set_name__(self, owner, name):
        self._nazwa_atrybutu = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self._nazwa_atrybutu, 0)

    def __set__(self, instance, value):
        if value < 0:
            value = 0
        instance.__dict__[self._nazwa_atrybutu] = value


class IteratorEkwipunku:
    def __init__(self, przedmioty):
        self._iterator = iter(przedmioty.values())

    def __next__(self):
        return next(self._iterator)

    def __iter__(self):
        return self


class Ekwipunek():
    def __init__(self):
        self.przedmioty = {}

    def __len__(self):
        return len(self.przedmioty)

    def __setitem__(self, key, value):
        self.przedmioty[key] = value

    def __getitem__(self, key):
        return self.przedmioty[key]

    def __delitem__(self, key):
        del self.przedmioty[key]

    def __repr__(self):
        return f"Lista przedmiotow gracza: {self.przedmioty}"

    def __iter__(self):
        return IteratorEkwipunku(self.przedmioty)


@total_ordering
class Gracz(Ekwipunek):
    liczba_graczy = 0

    def __init__(self, imie, hp, strategia=None):
        super().__init__()
        self.imie = imie
        self._hp = int(hp)
        self.strategia = strategia
        Gracz.liczba_graczy += 1

        if strategia is None:
            self.strategia = AtakMieczem()
        else:
            self.strategia = strategia

    def wykonaj_atak(self):
        print(f"{self.imie} atakuje: {self.strategia.atakuj()}")

    def zmien_strategie(self, nowa_strategia: StrategiaAtaku):
        self.strategia = nowa_strategia

    def pokaz_status_graczy(self):
        return f"liczba graczy: {self.liczba_graczy}"

    def przedstaw_sie(self):
        return f"Gracz {self.imie} (HP: {self.hp})"

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

    def __lt__(self, other):
        if not isinstance(other, Gracz):
            return NotImplemented
        return self.hp < other.hp


class Wojownik(Gracz, Bohater):
    sila = NieujemnaLiczba()

    def __init__(self, imie, hp, sila):
        super().__init__(imie, hp)
        self.sila = sila

    def przedstaw_sie(self):
        tekst = super().przedstaw_sie()
        return f"{tekst}, Sila: {self.sila}"

    def atak(self) -> int:
        return 10

    def opis(self) -> str:
        return "wojownik"

    def atak(self):
        if self.hp <= 0:
            raise BrakPunktowZdrowiaError("postac nie moze atakowac")
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
    mana = NieujemnaLiczba()

    def __init__(self, imie, hp, mana):
        super().__init__(imie, hp)
        self.mana = mana

    def przedstaw_sie(self):
        tekst = super().przedstaw_sie()
        return f"{tekst}, Mana: {self.mana}"


@dataclass
class PunktLekki:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


def fabryka_postaci(typ, imie):
    if typ == "wojownik":
        return Wojownik(imie, 120, 25)
    elif typ == "mag":
        return Mag(imie, 80, 50)
    else:
        raise ValueError(f"Typ {typ} nie istnieje")


gracz1 = Gracz("Artur", 100)
gracz1.__setitem__("Bron", "Ostrze gyatow")
print(gracz1.sprawdz_poprawnosc_imienia("Artur"))
gracz1.__setitem__("Ochrona", "tarcza")
print(gracz1.przedstaw_sie())
print(gracz1.przedmioty)
gracz = Gracz("Aragorn", 100, AtakKulaOgnia())
gracz.wykonaj_atak()

gracz2 = Gracz("Przemek", 120)
gracz2.hp = -100

woj1 = Wojownik("Garen", 25, 59)
woj2 = fabryka_postaci("wojownik", "Aatrox")

#  nieznany = fabryka_postaci("paladyn", "Netos")

fuzja = woj1 + woj2
print(fuzja.przedstaw_sie())

berserker = Wojownik.stworz_berserkera("Olaf")
print(berserker.przedstaw_sie(), "\n")

mag1 = fabryka_postaci("mag", "Nadeos")

druzyna = (gracz1, gracz2, mag1, woj1, woj2, berserker)
posortowani = sorted(druzyna, key=Gracz.przedstaw_sie)

print("Gracze posortowani alfabetycznie:")
for czlonek in posortowani:
    print(czlonek.przedstaw_sie())

print("\nPorównania gracz1 i gracz2: ")
print(gracz1 == gracz2)
print(gracz1 != gracz2)
print(gracz1 < gracz2)
print(gracz1 <= gracz2)
print(gracz1 > gracz2)
print(gracz1 >= gracz2)

ekw = Ekwipunek()
ekw["jedzenie"] = "jablko"
ekw["picie"] = "sok"
print("\nTest iteracji ekwipunku: ")

for przedmiot in ekw:
    print(przedmiot)

# p = PunktLekki(1, 2)
# print("\n")
# print(p.x)
# print(p.y)
#
# try:
#     p.z = 3
# except AttributeError as e:
#     print(e)
#
# try:
#     print(p.__dict__)
# except AttributeError as e:
#     print(e)
