from dataclasses import asdict
import sqlite3
from cars.interfaces import IDataAccess
from cars.models import NewCar, Auto


INSERT_NEW_CAR =('''
                 
insert into cars 
values (NULL, :make, :model, :color, :year, :price);
                 
''')

FILTER_CARS = ('''
               
select * from cars
where (:make is null or make like :make) and
      (:model is null or model like :model) and
      (:color is null or color like :color) and
      (:year_from is null or year >= :year_from) and
      (:year_to is null or year <= :year_to) and
      (:price_from is null or price >= :price_from) and
      (:price_to is null or price <= :price_to)
               
''')

class SQLiteDA(IDataAccess):
    def __init__(self, db):
        self.db = db

    def insert_car(self, new_car : NewCar):  
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            cur.execute(INSERT_NEW_CAR, asdict(new_car))
            conn.commit()

    def get_data(self, car_filter):
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            cur.execute(FILTER_CARS, asdict(car_filter))
            rows = list(cur.fetchall())
            return list(map(lambda row : Auto(*(row)), rows))
