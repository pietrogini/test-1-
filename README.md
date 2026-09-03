# test-1-

Primo progetto random — usato per imparare Git e sperimentare con GitHub Actions.

## Cosa c'è qui

- **`index.html`** — la mia prima pagina HTML, scritta a mano per imparare. Ha uno stile CSS con sfondo sfumato e una card centrata.
- **`scrape_libri.py`** — script Python che estrae titolo, prezzo e rating dei primi 20 libri da [books.toscrape.com](https://books.toscrape.com/) e li salva in `libri.csv`.
- **`libri.csv`** — output dello script sopra: 20 righe con `titolo`, `prezzo`, `rating`.
- **`.github/workflows/scrape.yml`** — workflow GitHub Actions che installa le dipendenze (`requests`, `beautifulsoup4`) ed esegue `scrape_libri.py`, caricando `libri.csv` come artifact. Si avvia solo manualmente dalla tab **Actions** ("Run workflow"), nessuna schedulazione automatica.

## Come eseguire lo scraper in locale

```bash
pip install requests beautifulsoup4
python3 scrape_libri.py
```
