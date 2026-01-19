import kalkulator
import pytest

def test_dodawania_liczb_dodatnich():
    assert kalkulator.dodaj(2, 3) == 5


def test_dodawania_liczb_ujemnych():
    assert kalkulator.dodaj(-2, -3) == -5

def test_dzielenia_przez_zero():
    with pytest.raises(ValueError):
        assert kalkulator.dziel(10, 0)

def test_poprawnego_dzielenia():
    assert kalkulator.dziel(10, 2) == 5


@pytest.mark.parametrize(
    "a, b, wynik",
    [
        (2, 3, 5),        # dwie liczby dodatnie
        (-2, -3, -5),    # dwie liczby ujemne
        (5, -3, 2),      # dodatnia i ujemna
        (7, 0, 7),       # liczba i zero
    ]
)
def test_dodawania_wielu_przypadkow(a, b, wynik):
    assert kalkulator.dodaj(a, b) == wynik
