from prettytable import PrettyTable
from cars.interfaces import IOutputBase

class PrettyConsole(IOutputBase):
    def print(self, autos):
        table = PrettyTable()
        table.field_names = ["Id", "Markė", "Modelis", "Spalve", "Metai", "Kaina"]
        table.add_rows(list(map(lambda auto: [ auto.id, auto.make, auto.model, auto.color, auto.year, auto.price ], autos)))
        print(table)