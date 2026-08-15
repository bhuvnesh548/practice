def greater(a, b):
        if data[a]["population"] > data[b]["population"]:
              return a
        elif data[a]["population"] < data[b]["population"]:
              return b
        else: return None;

import random, os;
data = {
    "India": {"population": 1476.0, "continent": "Asia"},
    "China": {"population": 1412.0, "continent": "Asia"},
    "United States": {"population": 349.0, "continent": "North America"},
    "Indonesia": {"population": 287.0, "continent": "Asia"},
    "Pakistan": {"population": 259.0, "continent": "Asia"},
    "Nigeria": {"population": 242.0, "continent": "Africa"},
    "Brazil": {"population": 213.0, "continent": "South America"},
    "Bangladesh": {"population": 177.0, "continent": "Asia"},
    "Russia": {"population": 143.0, "continent": "Europe"},
    "Ethiopia": {"population": 138.0, "continent": "Africa"},
    "Mexico": {"population": 132.0, "continent": "North America"},
    "Japan": {"population": 122.0, "continent": "Asia"},
    "Egypt": {"population": 120.0, "continent": "Africa"},
    "Philippines": {"population": 117.0, "continent": "Asia"},
    "DR Congo": {"population": 116.0, "continent": "Africa"},
    "Vietnam": {"population": 102.0, "continent": "Asia"},
    "Iran": {"population": 89.5, "continent": "Asia"},
    "Turkey": {"population": 86.2, "continent": "Asia"},
    "Germany": {"population": 84.5, "continent": "Europe"},
    "Thailand": {"population": 71.9, "continent": "Asia"},
    "United Kingdom": {"population": 69.1, "continent": "Europe"},
    "Tanzania": {"population": 68.5, "continent": "Africa"},
    "France": {"population": 66.5, "continent": "Europe"},
    "South Africa": {"population": 64.0, "continent": "Africa"},
    "Italy": {"population": 59.2, "continent": "Europe"},
    "Kenya": {"population": 56.2, "continent": "Africa"},
    "South Korea": {"population": 51.7, "continent": "Asia"},
    "Colombia": {"population": 52.3, "continent": "South America"},
    "Spain": {"population": 47.9, "continent": "Europe"},
    "Argentina": {"population": 46.0, "continent": "South America"},
    "Algeria": {"population": 46.8, "continent": "Africa"},
    "Iraq": {"population": 46.0, "continent": "Asia"},
    "Sudan": {"population": 49.0, "continent": "Africa"},
    "Uganda": {"population": 49.5, "continent": "Africa"},
    "Canada": {"population": 39.5, "continent": "North America"},
    "Poland": {"population": 37.6, "continent": "Europe"},
    "Morocco": {"population": 38.0, "continent": "Africa"},
    "Saudi Arabia": {"population": 37.0, "continent": "Asia"},
    "Ukraine": {"population": 37.9, "continent": "Europe"},
    "Angola": {"population": 37.8, "continent": "Africa"},
    "Uzbekistan": {"population": 36.4, "continent": "Asia"},
    "Yemen": {"population": 35.2, "continent": "Asia"},
    "Peru": {"population": 34.4, "continent": "South America"},
    "Malaysia": {"population": 34.6, "continent": "Asia"},
    "Ghana": {"population": 34.4, "continent": "Africa"},
    "Mozambique": {"population": 34.8, "continent": "Africa"},
    "Nepal": {"population": 31.0, "continent": "Asia"},
    "Madagascar": {"population": 31.2, "continent": "Africa"},
    "Ivory Coast": {"population": 29.8, "continent": "Africa"},
    "Venezuela": {"population": 29.4, "continent": "South America"},
    "Cameroon": {"population": 29.4, "continent": "Africa"},
    "Niger": {"population": 28.2, "continent": "Africa"},
    "Australia": {"population": 26.8, "continent": "Oceania"},
    "North Korea": {"population": 26.2, "continent": "Asia"},
    "Taiwan": {"population": 23.9, "continent": "Asia"},
    "Mali": {"population": 24.5, "continent": "Africa"},
    "Syria": {"population": 24.3, "continent": "Asia"},
    "Sri Lanka": {"population": 21.9, "continent": "Asia"},
    "Kazakhstan": {"population": 20.5, "continent": "Asia"},
    "Chile": {"population": 19.6, "continent": "South America"},
    "Romania": {"population": 19.0, "continent": "Europe"},
    "Netherlands": {"population": 18.0, "continent": "Europe"},
    "Guatemala": {"population": 18.3, "continent": "North America"},
    "Ecuador": {"population": 18.2, "continent": "South America"},
    "Cambodia": {"population": 17.0, "continent": "Asia"},
    "Senegal": {"population": 18.2, "continent": "Africa"},
    "Chad": {"population": 18.8, "continent": "Africa"},
    "Somalia": {"population": 18.7, "continent": "Africa"},
    "Zimbabwe": {"population": 17.1, "continent": "Africa"},
    "Guinea": {"population": 14.5, "continent": "Africa"},
    "Rwanda": {"population": 14.4, "continent": "Africa"},
    "Benin": {"population": 14.1, "continent": "Africa"},
    "Burundi": {"population": 13.6, "continent": "Africa"},
    "Tunisia": {"population": 12.5, "continent": "Africa"},
    "Bolivia": {"population": 12.5, "continent": "South America"},
    "Belgium": {"population": 11.9, "continent": "Europe"},
    "Haiti": {"population": 11.9, "continent": "North America"},
    "Cuba": {"population": 11.0, "continent": "North America"},
    "South Sudan": {"population": 11.3, "continent": "Africa"},
    "Dominican Republic": {"population": 11.4, "continent": "North America"},
    "Czech Republic": {"population": 10.9, "continent": "Europe"},
    "Greece": {"population": 10.3, "continent": "Europe"},
    "Sweden": {"population": 10.6, "continent": "Europe"},
    "Portugal": {"population": 10.2, "continent": "Europe"},
    "Azerbaijan": {"population": 10.4, "continent": "Asia"},
    "Hungary": {"population": 9.6, "continent": "Europe"},
    "Honduras": {"population": 10.6, "continent": "North America"},
    "Israel": {"population": 9.9, "continent": "Asia"},
    "Tajikistan": {"population": 10.5, "continent": "Asia"},
    "Belarus": {"population": 9.1, "continent": "Europe"},
    "Austria": {"population": 9.1, "continent": "Europe"},
    "Switzerland": {"population": 8.9, "continent": "Europe"},
    "Papua New Guinea": {"population": 10.5, "continent": "Oceania"},
    "United Arab Emirates": {"population": 9.5, "continent": "Asia"},
    "Jordan": {"population": 11.4, "continent": "Asia"},
    "Serbia": {"population": 7.1, "continent": "Europe"},
    "Hong Kong": {"population": 7.5, "continent": "Asia"},
    "Libya": {"population": 7.0, "continent": "Africa"},
    "Bulgaria": {"population": 6.7, "continent": "Europe"},
    "Paraguay": {"population": 6.9, "continent": "South America"},
    "El Salvador": {"population": 6.4, "continent": "North America"},
    "Singapore": {"population": 6.1, "continent": "Asia"},
    "Denmark": {"population": 6.0, "continent": "Europe"},
    "Finland": {"population": 5.6, "continent": "Europe"},
    "Norway": {"population": 5.5, "continent": "Europe"},
    "Slovakia": {"population": 5.4, "continent": "Europe"},
    "Ireland": {"population": 5.3, "continent": "Europe"},
    "New Zealand": {"population": 5.3, "continent": "Oceania"},
    "Costa Rica": {"population": 5.2, "continent": "North America"},
    "Lebanon": {"population": 5.3, "continent": "Asia"},
    "Oman": {"population": 4.7, "continent": "Asia"},
    "Panama": {"population": 4.5, "continent": "North America"},
    "Kuwait": {"population": 4.3, "continent": "Asia"},
    "Croatia": {"population": 4.0, "continent": "Europe"},
    "Georgia": {"population": 3.7, "continent": "Asia"},
    "Uruguay": {"population": 3.4, "continent": "South America"},
    "Mongolia": {"population": 3.5, "continent": "Asia"},
    "Armenia": {"population": 2.8, "continent": "Asia"},
    "Albania": {"population": 2.8, "continent": "Europe"},
    "Lithuania": {"population": 2.9, "continent": "Europe"},
    "Qatar": {"population": 2.7, "continent": "Asia"},
    "Jamaica": {"population": 2.8, "continent": "North America"},
    "Slovenia": {"population": 2.1, "continent": "Europe"},
    "Latvia": {"population": 1.9, "continent": "Europe"},
    "Bahrain": {"population": 1.5, "continent": "Asia"},
    "Estonia": {"population": 1.4, "continent": "Europe"},
    "Cyprus": {"population": 1.3, "continent": "Europe"},
    "Fiji": {"population": 0.9, "continent": "Oceania"},
    "Bhutan": {"population": 0.8, "continent": "Asia"},
    "Luxembourg": {"population": 0.7, "continent": "Europe"},
    "Montenegro": {"population": 0.6, "continent": "Europe"},
    "Malta": {"population": 0.5, "continent": "Europe"},
    "Maldives": {"population": 0.5, "continent": "Asia"},
    "Iceland": {"population": 0.4, "continent": "Europe"}
}
has_lost = False;
lComp = random.sample(list(data), 2)
print(lComp);
a = lComp[0]
b = lComp[1]
while not has_lost:
    choice = input(f'''Compare:
        {a}, a country in {data[a]["continent"]}
        and
        {b}, a country in {data[b]["continent"]}
        who has more population, a or b?: |''').lower();

    """match choice:
        case 'a': inp = a;
        case 'b': inp = b;
        case 'n': inp = None;
    if greater(a, b) is not None:
          if"""

    if data[a]["population"] > data[b]["population"]:
        if choice == 'b':
            has_lost = True

    if data[a]["population"] < data[b]["population"]:
        if choice == 'a':
            has_lost = True;
    else:
        a = b;
        b = random.choice(list(data))
        print("you won!")
        os.system("cls")
print("you lost")
os.system("cls")

Vidhus_name = ["Sharmili", "Hitler 2.0", "heart
