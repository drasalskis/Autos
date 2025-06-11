import random
from dependency_injector import containers, providers
from cars.output import SimpleConsole, PrettyConsole
from cars.data_access import SQLiteDA
from cars.cars import Cars

class Container(containers.DeclarativeContainer):
    data_access = providers.Factory(SQLiteDA, db="autos.db")    

    output = providers.Singleton(PrettyConsole)

    cars = providers.Singleton(
        Cars,
        data_access,
        output
    )    
