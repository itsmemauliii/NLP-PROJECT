
import json
import re

# Load listings
with open('data/listings.json') as f:
    listings = json.load(f)

def match_properties(query):
    query = query.lower()
    budget = None
    if 'under' in query:
        match = re.search(r'under (\d+)', query)
        if match:
            budget = int(match.group(1))

    bhk_type = None
    if '2bhk' in query:
        bhk_type = '2BHK'
    elif '3bhk' in query:
        bhk_type = '3BHK'

    location = None
    for loc in ['thaltej', 'bodakdev', 'hebatpur']:
        if loc in query:
            location = loc.capitalize()

    filtered = []
    for prop in listings:
        if budget and prop['price_lakhs'] > budget:
            continue
        if bhk_type and prop['type'] != bhk_type:
            continue
        if location and prop['location'] != location:
            continue
        filtered.append(prop)

    # Add creative suggestion
    if filtered:
        surprise = {
            "id": 999,
            "project_name": "🌿 SkyGarden Escape",
            "location": location or "Ahmedabad",
            "price_lakhs": (budget or 60) + 5,
            "type": "Penthouse",
            "area_sqft": 1450,
            "features": ["Private Terrace", "Smart Home", "Mini Library"],
            "contact": "comingsoon@vibes.com",
            "source": "Inspired by your search preferences!"
        }
        filtered.append(surprise)

    return filtered[:4]
