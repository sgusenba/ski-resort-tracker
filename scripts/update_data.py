import json
import datetime
import os

from scraper_v4 import scrape_resort
from resorts import RESORTS
from season import season_active

DATA_FILE = "data/history.json"

def load():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as f:
        return json.load(f)

def save(data):
    with open(DATA_FILE,"w") as f:
        json.dump(data,f,indent=2)

def run():

    history = load()

    if not season_active(history):
        print("Season ended")
        return

    today = datetime.date.today().isoformat()

    entry = {"date":today,"resorts":[]}

    for r in RESORTS.values():

        entry["resorts"].append(
            scrape_resort(r["name"])
        )

    history.append(entry)

    save(history)

if __name__ == "__main__":
    run()
