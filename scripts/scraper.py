import requests
from bs4 import BeautifulSoup

def scrape(url, name):

    r = requests.get(url, timeout=20)
    soup = BeautifulSoup(r.text, "html.parser")

    lifts_open = 0
    lifts_total = 0
    slopes_open = 0
    slopes_total = 0

    for el in soup.find_all(["tr","li","div"]):

        text = el.get_text().lower()

        if "lift" in text:
            lifts_total += 1
            if "geöffnet" in text or "open" in text:
                lifts_open += 1

        if "piste" in text or "slope" in text:
            slopes_total += 1
            if "geöffnet" in text or "open" in text:
                slopes_open += 1

    return {
        "resort": name,
        "lifts_open": lifts_open,
        "lifts_total": lifts_total,
        "slopes_open": slopes_open,
        "slopes_total": slopes_total
    }
