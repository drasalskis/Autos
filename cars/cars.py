import pyinputplus as pyip
from cars.models import CarFilter, NewCar
from cars.interfaces import IOutputBase, IDataAccess, ICars

class Cars(ICars):
    def __init__ (self, data_access : IDataAccess, output: IOutputBase):
        self.data_access = data_access
        self.output = output
    
    def run(self):
        while True:
            print("\n1-sukurti naują 2-peržiūrėti, 3-išeiti\n")
            option = pyip.inputChoice(["1", "2", "3"], prompt="Pasirinkite norimą veiksmą: ")
            match option:
                case "1": 
                    new_car = self.__inputNewCar()
                    self.data_access.insert_car(new_car)
                case "2":
                    car_filter = self.__inputCarFilters()
                    autos = self.data_access.get_data(car_filter)
                    self.output.print(autos)
                case "3": break
                case _: print("Veiksmas negalimas")  


    def __inputNewCar(self) -> NewCar:
        print("Įveskite naujo automobilio parametrus:")
        make = pyip.inputStr("Įveskite markę: ")
        model = pyip.inputStr("Įveskite modelį: ")
        color = pyip.inputStr("Įveskite spalvą: ")
        year = pyip.inputInt("Įveskite pagaminimo metus: ")
        price = pyip.inputFloat("Įveskite kainą: ") 

        return NewCar(make, model, color, year, price)       


    def __inputCarFilters(self) -> CarFilter:
        print("Įveskite ieškomo automobilio parametrus:")
        make = pyip.inputStr("Įveskite markę: ", blank=True) or None
        model = pyip.inputStr("Įveskite modelį: ", blank=True) or None
        color = pyip.inputStr("Įveskite spalvą: ", blank=True) or None
        year_from = pyip.inputInt("Įveskite pagaminimo metus nuo: ", blank=True) or 0
        year_to = pyip.inputInt("Įveskite pagaminimo metus iki: ", blank=True, greaterThan=year_from) or None
        price_from = pyip.inputFloat("Įveskite kainą nuo: ", blank=True) or 0
        price_to = pyip.inputFloat("Įveskite kainą iki: ", blank=True, greaterThan=price_from) or None

        return CarFilter(make, model, color, year_from, year_to, price_from, price_to)         