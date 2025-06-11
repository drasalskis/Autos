from abc import ABC

from cars.models import NewCar, CarFilter

class IDataAccess(ABC):
    def insert_car(self, new_car : NewCar):
        pass

    def get_data(self, car_filter: CarFilter):
        pass

    def get_data1(self, car_filter: CarFilter):
        pass    