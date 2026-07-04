import requests
import random
from modals import MyPlace

def get_places_country(country):
    url='https://nominatim.openstreetmap.org/search'
    headers = {
        "User-Agent": "CafeApp/1.0"
    }

    photos = [
        '/static/img/cafe1.png',
        '/static/img/cafe2.png',
        '/static/img/cafe3.png',
        '/static/img/cafe4.png',
        '/static/img/cafe5.png',
        '/static/img/cafe6.png',
        '/static/img/cafe7.png',
        '/static/img/cafe8.png',
        '/static/img/cafe9.png',
    ]

    index = 0
    places = []

    for amntity in ['cafe', 'restaurant']:
        params = {
            'country': country,
            'amenity': amntity,
            'format': 'json',
            'limit': 40,
        }

        res = requests.get(url, params=params,headers = headers)  
        data = res.json()
    
        for item in data:
            photo = photos[index % len(photos)]
            index += 1

            places.append(
                {
                    'id': f"osm_{item.get('osm_id')}",
                    'title': item.get('name'),
                    'address': item.get('display_name', ''),
                    'lat': item.get('lat'),
                    'lon': item.get('lon'),
                    'type': amntity,
                    'rating': random.randint(10,50)/10,
                    'photo': photo,
                    'is_favorite': 0
                }
            )
    return places

def get_places(city):
    url = "https://nominatim.openstreetmap.org/search"
    headers = {"User-Agent": "CafeApp/1.0"}

    photos = [
        '/static/img/cafe1.png',
        '/static/img/cafe2.png',
        '/static/img/cafe3.png',
        '/static/img/cafe4.png',
        '/static/img/cafe5.png',
        '/static/img/cafe6.png',
        '/static/img/cafe7.png',
        '/static/img/cafe8.png',
        '/static/img/cafe9.png',
    ]

    index = 0
    places = []
    

    for amenity in ["cafe", "restaurant"]:
        params = {
            "city": city,
            "amenity": amenity,
            "format": "json",
            "limit": 40,
        }

        res = requests.get(url, params=params, headers=headers)
        data = res.json()

        for item in data:
            title = item.get("name") or item.get("display_name")

            photo = photos[index % len(photos)]
            index += 1

            places.append({
                'id': f"osm_{item.get('osm_id')}",
                "title": title,
                "address": item.get("display_name"),
                "lat": item.get("lat"),
                "lon": item.get("lon"),
                "type": amenity,
                "rating": random.randint(10, 50) / 10,
                "photo": photo,
                'is_favorite': 0
            })

    return places

def geocode_address(address: str):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
        "limit": 1
    }
    headers = {"User-Agent": "CafeApp/1.0"}

    res = requests.get(url, params=params, headers=headers)
    data = res.json()

    if not data:
        return None, None

    return float(data[0]["lat"]), float(data[0]["lon"])


def add_place(session, filename, title, address, rating):
    lat, lon = geocode_address(address)
    
    new_place = MyPlace(
        photo=filename,
        title=title,
        address=address,
        rating=rating,
        lat=lat,
        lon=lon
    )

    session.add(new_place)
    session.commit()
