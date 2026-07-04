<p align="center">
  <img src="images/banner_top.png" alt="Caffee Banner Top" width="100%">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=160&color=custom_gradient=0:8D6748,10:B5835A,100:D9A567&text=Cafe Rest&fontAlignY=40&fontColor=FFFFFF" alt="Cafe & Rest Capsule"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Flask-3.1-000000?logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?logo=sqlalchemy&logoColor=white">
  <img src="https://img.shields.io/badge/Leaflet.js-1.9-199900?logo=leaflet&logoColor=white">
  <img src="https://img.shields.io/badge/OpenStreetMap-Nominatim-7EBC6F?logo=openstreetmap&logoColor=white">
</p>

---

# ☕ Cafe & Rest

**Cafe & Rest** — веб-приложение на Flask для поиска кафе и ресторанов на интерактивной карте. Данные о заведениях подтягиваются из OpenStreetMap (Nominatim), а пользователь может добавлять свои места, ставить оценки и сохранять понравившиеся точки в избранное.

## ✨ Основные возможности

- 🗺️ Интерактивная карта заведений на Leaflet.js
- 🔍 Поиск кафе и ресторанов по городу через OpenStreetMap Nominatim
- ⭐ Избранное — как для мест из OSM, так и для добавленных пользователем
- ➕ Добавление своего заведения с фото, адресом и рейтингом
- 📍 Автоматическое геокодирование адреса в координаты
- 💾 Хранение данных в SQLite через SQLAlchemy ORM

---

## 📸 Скриншоты

### 🏠 Главная страница

Карта с заведениями и список места слева. Можно искать по городу, переключаться между всеми местами, своими и избранными.

<p align="center">
  <img src="images/main_page.png" alt="Main Page" width="90%">
</p>

---

### ➕ Добавление места

Пользователь может загрузить фото своего заведения, указать название, адрес и рейтинг — адрес автоматически геокодируется и попадает на карту.

<p align="center">
  <img src="images/add_place.png" alt="Add Place Page" width="70%">
</p>

---

## 🛠️ Стек технологий

| Слой       | Технология                  |
| ---------- | --------------------------- |
| Backend    | Flask                       |
| ORM / БД   | SQLAlchemy + SQLite         |
| Карта      | Leaflet.js                  |
| Гео-данные | OpenStreetMap Nominatim API |

## 📂 Структура проекта

```
.
├── app.py            # Flask-приложение и маршруты
├── modals.py         # Модели SQLAlchemy (MyPlace, FavoritePlace)
├── utils.py          # Работа с Nominatim API и геокодирование
├── settings.py        # Настройки (имя БД)
├── templates/         # HTML-шаблоны (Jinja2)
├── static/            # CSS, изображения, загруженные фото
└── database.db        # SQLite база данных
```

## 🚀 Запуск

```bash
pip install -r requirements.txt
python app.py
```

Приложение будет доступно на **http://localhost:5000**
