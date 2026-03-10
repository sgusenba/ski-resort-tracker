import requests
from bs4 import BeautifulSoup
import re


def extract_number(pattern, text):
    m = re.search(pattern, text, re.IGNORECASE)
    if m:
        return int(m.group(1))
    return None


def extract_pair(pattern, text):
    m = re.search(pattern, text, re.IGNORECASE)
    if m:
        return int(m.group(1)), int(m.group(2))
    return None, None


def scrape_resort(url, name):

    r = requests.get(url, timeout=20)
    soup = BeautifulSoup(r.text, "html.parser")
    text = soup.get_text(" ", strip=True)

    # --- lifts ---
    lifts_open, lifts_total = extract_pair(
        r"Lifte\s*(\d+)\s*/\s*(\d+)", text
    )

    # --- slopes ---
    slopes_open, slopes_total = extract_pair(
        r"Pisten\s*(\d+)\s*/\s*(\d+)", text
    )

    # --- snow height ---
    snow_valley = extract_number(
        r"Schneehöhe\s*Tal\s*(\d+)\s*cm", text
    )

    snow_mountain = extract_number(
        r"Schneehöhe\s*Berg\s*(\d+)\s*cm", text
    )

    # --- new snow ---
    new_snow_24 = extract_number(
        r"Neuschnee\s*24h\s*(\d+)\s*cm", text
    )

    new_snow_7 = extract_number(
        r"Neuschnee\s*7\s*Tage\s*(\d+)\s*cm", text
    )

    # --- open slope kilometers ---
    slope_km_open = extract_number(
        r"(\d+)\s*km\s*Pisten\s*offen", text
    )

    # --- avalanche level ---
    avalanche = extract_number(
        r"Lawinenwarnstufe\s*(\d)", text
    )

    return {
        "resort": name,
        "lifts_open": lifts_open,
        "lifts_total": lifts_total,
        "slopes_open": slopes_open,
        "slopes_total": slopes_total,
        "snow_valley_cm": snow_valley,
        "snow_mountain_cm": snow_mountain,
        "new_snow_24h_cm": new_snow_24,
        "new_snow_7d_cm": new_snow_7,
        "slope_km_open": slope_km_open,
        "avalanche_level": avalanche
    }
