from abc import ABC, abstractmethod

from cars.models import NewCar, CarFilter

class IDataAccess(ABC):
    @abstractmethod
    def insert_car(self, new_car : NewCar):
        pass
    
    @abstractmethod
    def get_data(self, car_filter: CarFilter):
        pass