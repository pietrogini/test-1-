"""Estrae titolo, prezzo e rating dei primi 20 libri da books.toscrape.com."""

import csv

import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"
RATING_WORDS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def scrape_libri(url: str, limit: int = 20) -> list[dict]:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    libri = []
    for articolo in soup.select("article.product_pod")[:limit]:
        titolo = articolo.h3.a["title"]
        prezzo = articolo.select_one(".price_color").get_text(strip=True)
        rating_classe = articolo.select_one("p.star-rating")["class"][1]
        rating = RATING_WORDS.get(rating_classe, 0)
        libri.append({"titolo": titolo, "prezzo": prezzo, "rating": rating})

    return libri


def salva_csv(libri: list[dict], percorso: str) -> None:
    with open(percorso, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["titolo", "prezzo", "rating"])
        writer.writeheader()
        writer.writerows(libri)


if __name__ == "__main__":
    libri = scrape_libri(URL)
    salva_csv(libri, "libri.csv")

    print(f"Salvati {len(libri)} libri in libri.csv\n")
    print(f"{'Titolo':<45} {'Prezzo':>8} {'Rating':>7}")
    for libro in libri:
        print(f"{libro['titolo']:<45} {libro['prezzo']:>8} {libro['rating']:>7}")
