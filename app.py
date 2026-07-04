from flask import Flask, render_template, request, redirect, jsonify
from utils import get_places_country, get_places, add_place
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import settings
from modals import MyPlace, FavoritePlace

app = Flask(__name__)
engine = create_engine(f'sqlite:///{settings.DATABASE_NAME}')
Ssesion = sessionmaker(bind=engine)

@app.route('/')
def main():
    mode = request.args.get('mode', 'all')
    city = request.args.get('city')

    session = Ssesion()
    user_places = session.query(MyPlace).all()
    session.close()

    places_user = [
        {
            "id": p.id,
            "title": p.title,
            "address": p.address,
            "rating": p.rating,
            "photo": f"/static/uploads/{p.photo}",
            "lat": p.lat,
            "lon": p.lon,
            "type": "user",
            "is_favorite": p.is_favorite
        }
        for p in user_places
    ]

    if mode == "mine":
        if city and city.strip():
            filtered = [
                place for place in places_user
                if city.lower() in place["address"].lower()
            ]
            places = filtered
        else:
            places = places_user

    elif mode == 'favorite':
        session = Ssesion()
        fav_osm = session.query(FavoritePlace).all()
        session.close()

        fav_osm_places = [
            {
                "id": f.place_id,
                "title": f.title,
                "address": f.address,
                "rating": f.rating,
                "photo": f.photo,
                "lat": f.lat,
                "lon": f.lon,
                "type": "osm",
                "is_favorite": 1
            }
            for f in fav_osm
        ]

        fav_user_places = [p for p in places_user if p["is_favorite"] == 1]
        places = fav_osm_places + fav_user_places

    else:
        if city and city.strip():
            places_osm = get_places(city.strip())
        else:
            places_osm = get_places_country('Russia')

        session = Ssesion()
        fav_ids = {f.place_id for f in session.query(FavoritePlace.place_id).all()}
        session.close()

        for p in places_osm:
            p["is_favorite"] = 1 if p["id"] in fav_ids else 0

        places = places_osm + places_user

    return render_template('index.html', places=places, mode=mode)


@app.route('/favorite/<place_id>', methods=['POST'])
def favorite(place_id):
    session = Ssesion()

    if place_id.startswith("osm_"):
        fav = session.query(FavoritePlace).filter_by(place_id=place_id).first()

        if fav:
            session.delete(fav)
            is_favorite = False
        else:
            city = request.args.get('city')
            if city and city.strip():
                places_osm = get_places(city.strip())
            else:
                places_osm = get_places_country('Russia')

            place_data = next((p for p in places_osm if p["id"] == place_id), None)

            if place_data:
                new_fav = FavoritePlace(
                    place_id=place_id,
                    title=place_data["title"],
                    address=place_data["address"],
                    rating=place_data["rating"],
                    photo=place_data["photo"],
                    lat=place_data["lat"],
                    lon=place_data["lon"]
                )
                session.add(new_fav)
            is_favorite = True

        session.commit()
        session.close()
        return jsonify({"is_favorite": is_favorite})
    else:
        place = session.query(MyPlace).get(int(place_id))
        place.is_favorite = 0 if place.is_favorite else 1
        is_favorite = bool(place.is_favorite)
        session.commit()
        session.close()
        return jsonify({"is_favorite": is_favorite})


@app.route('/add_place', methods = ["GET","POST"])
def add_page():
    if request.method == 'POST':
        session = Ssesion()
        photo_file = request.files.get('photo')
        filename = photo_file.filename
        photo_file.save(f"static/uploads/{filename}")
        title = request.form.get('title')
        address = request.form.get('address')
        rating = float(request.form.get('rating'))
        add_place(session, filename, title, address, rating)
        return redirect('/')
    return render_template('add_place.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)