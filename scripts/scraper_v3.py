import requests
from bs4 import BeautifulSoup
import json


def scrape_resort(url, name):

    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=20
    )

    soup = BeautifulSoup(r.text, "html.parser")

    lifts_open = None
    lifts_total = None
    slopes_open = None
    slopes_total = None
    slopes_km_open = None
    slopes_km_total = None
    valley_run = None

    # Find structured JSON data
    scripts = soup.find_all("script", type="application/ld+json")

    for s in scripts:

        try:
            data = json.loads(s.string)

            if isinstance(data, dict):

                text = json.dumps(data)

                # Lifts
                import re
                m = re.search(r"(\d+)\s*von\s*(\d+)\s*Lifte", text)
                if m:
                    lifts_open = int(m.group(1))
                    lifts_total = int(m.group(2))

                # Slopes count
                m = re.search(r"(\d+)\s*von\s*(\d+)\s*Pisten", text)
                if m:
                    slopes_open = int(m.group(1))
                    slopes_total = int(m.group(2))

                # Slopes km
                m = re.search(r"([\d,]+)\s*km\s*von\s*([\d,]+)\s*km", text)
                if m:
                    slopes_km_open = float(m.group(1).replace(",", "."))
                    slopes_km_total = float(m.group(2).replace(",", "."))

                # Valley run
                m = re.search(r"Talabfahrt\s*:?\\s*(fahrbar|geschlossen)", text)
                if m:
                    valley_run = m.group(1)

        except:
            pass

    return {
        "resort": name,
        "lifts_open": lifts_open,
        "lifts_total": lifts_total,
        "slopes_open": slopes_open,
        "slopes_total": slopes_total,
        "slopes_km_open": slopes_km_open,
        "slopes_km_total": slopes_km_total,
        "valley_run": valley_run
    }
