from pathlib import Path
from datetime import date

folder =  Path('raporty_dzienne')

sciezka = folder / str(date.today()) / "raport txt"

sciezka.parent.mkdir(parents=True, exist_ok=True)

tresc_raportu = f"raport z dnia {sciezka} \n wszystko w porzasiu"
sciezka.write_text(tresc_raportu)

print(tresc_raportu)