class NiewystarczajaceSrodki(Exception):
    pass


class Portfel:
    saldo: float

    def __init__(self) -> None:
        self.saldo = 0.0

    def wplata(self, kwota: float) -> None:
        if kwota <= 0:
            raise ValueError("Kwota musi być dodatnia")
        self.saldo += kwota

    def wyplata(self, kwota: float) -> None:
        if kwota > self.saldo:
            raise NiewystarczajaceSrodki("Brak środków w portfelu")
        self.saldo -= kwota
