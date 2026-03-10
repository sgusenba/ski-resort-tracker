import requests
from bs4 import BeautifulSoup
import re


def find_value(label, text):

    pattern = label + r"\s*([^\n]+)"
    m = re.search(pattern, text, re.IGNORECASE)

    if m:
        return m.group(1).strip()

    return None


def parse_fraction(text):

    m = re.search(r"(\d+)\s*von\s*(\d+)", text)
    if m:
        return int(m.group(1)), int(m.group(2))

    return None, None


def parse_km(text):

    m = re.search(r"([\d,]+)\s*km\s*von\s*([\d,]+)\s*km", text)

    if m:
        open_km = float(m.group(1).replace(",", "."))
        total_km = float(m.group(2).replace(",", "."))
        return open_km, total_km

    return None, None


def scrape_resort(url, name):

    r = requests.get(url, timeout=20)
    soup = BeautifulSoup(r.text, "html.parser")

    text = soup.get_text("\n", strip=True)

    # --- LIFTS ---
    lifts_line = find_value("Offene Lifte", text
