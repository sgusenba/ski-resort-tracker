import requests


RESORT_API = {
    "Kasberg": "https://api.bergfex.com/v2/snowreport/gruenau-kasberg",
    "Feuerkogel": "https://api.bergfex.com/v2/snowreport/feuerkogel",
    "Gosau": "https://api.bergfex.com/v2/snowreport/gosau",
    "Werfenweng": "https://api.bergfex.com/v2/snowreport/werfenweng"
}


def scrape_resort(name):

    url = RESORT_API[name]

    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=20
    )

    data = r.json()

    lifts_open = data["lifts"]["open"]
    lifts_total = data["lifts"]["total"]

    slopes_open = data["slopes"]["open"]
    slopes_total = data["slopes"]["total"]

    slopes_km_open = data["slopes"]["km_open"]
    slopes_km_total = data["slopes"]["km_total"]

    valley_run = data.get("valley_run")

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
