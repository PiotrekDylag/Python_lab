import requests

def pobierz_cene_euro():
    url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/?format=json"
    response = requests.get(url)
    dane = response.json()
    return dane["rates"][0]["mid"]
