import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta
from enum import Enum



date = "2025-06-30"
class Canteen(Enum):
    Flugplatz = 38420
    Rempartstraße = 1
    Institutsviertel = 2
    Littenweiler = 3

canteen = Canteen.Rempartstraße


def fetch_menu(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text

def parse_menu(html, canteen:Canteen, date:str):
    soup = BeautifulSoup(html, "html.parser")
    dishes = []

    items = soup.select('a[href^="/meal/"]') 
    for item in items:
        img_tag = item.select_one("img")
        if not img_tag or not img_tag.get("src"):
            continue  # überspringe ohne Bild

        img_url = img_tag["src"]
        name = item.select_one(".font-semibold span").text.strip()
        ingredients = item.select_one(".text-sm p").get_text(separator=', ', strip=True)

        dishes.append({
            "name": name,
            "ingredients": ingredients,
            "image_url": f"https://mensa.fachschaft.tf{img_url}",
            "canteen": canteen.name,
            "date": date
        })

    return dishes

def save_json(data, filename="menu.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def scrapeFor(canteen, date):
    URL = f"https://mensa.fachschaft.tf/?view=week&canteen={canteen.value}&date={date}"
    html = fetch_menu(URL)
    dishes = parse_menu(html, canteen, date)
    print(f"Found dishes for {canteen.name} ({date}): {len(dishes)}")
    return dishes

def main():
    today = datetime.now()
    dishes = []
    for i in range(104):
        date_delta = today - timedelta(weeks=i)
        date = date_delta.strftime("%Y-%m-%d")
        for canteen in Canteen:
           dishes.append(scrapeFor(canteen, date))
    save_json(dishes)



if __name__ == "__main__":
    main()