import settings
from sqlalchemy import create_engine, Column, Text, Integer,Float
from sqlalchemy.orm import declarative_base, sessionmaker

BaseModel = declarative_base()

class MyPlace(BaseModel):
    __tablename__ = 'my_place'

    id = Column(Integer, primary_key=True)
    photo = Column(Text)
    title = Column(Text)
    address = Column(Text)
    rating = Column(Float)
    lat = Column(Float)
    lon = Column(Float)
    is_favorite = Column(Integer, default=0)

    def __repr__(self):
        return f'<Место: {self.rating} {self.address}>'

class FavoritePlace(BaseModel):
    __tablename__ = "favorite_place"

    id = Column(Integer, primary_key=True)
    place_id = Column(Text)
    title = Column(Text)
    address = Column(Text)
    rating = Column(Float)
    photo = Column(Text)
    lat = Column(Float)
    lon = Column(Float)


if __name__ == '__main__':
    engine = create_engine(f'sqlite:///{settings.DATABASE_NAME}')
    BaseModel.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    all_pizza = session.query(MyPlace).all()
    for pizza in all_pizza:
        print(pizza)
    session.close()