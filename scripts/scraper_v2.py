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

    if not text:
        return None, None

    m = re.search(r"(\d+)\s*von\s*(\d+)", text)

    if m:
        return int(m.group(1)), int(m.group(2))

    return None, None


def parse_km(text):

    if not text:
        return None, None

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

    # Offene Lifte
    lifts_line = find_value("Offene Lifte", text)
    lifts_open, lifts_total = parse_fraction(lifts_line)

    # Offene Pisten km
    slopes_km_line = find_value("Offene Pisten", text)
    slopes_km_open, slopes_km_total = parse_km(slopes_km_line)

    # Pisten Anzahl
    slopes_count_open, slopes_count_total = parse_fraction(slopes_km_line)

    # Talabfahrt
    valley_run = find_value("Talabfahrt", text)

    return {
        "resort": name,
        "lifts_open": lifts_open,
        "lifts_total": lifts_total,
        "slopes_open": slopes_count_open,
        "slopes_total": slopes_count_total,
        "slopes_km_open": slopes_km_open,
        "slopes_km_total": slopes_km_total,
        "valley_run": valley_run
    }
