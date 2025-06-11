from cars.interfaces.output_base import IOutputBase

class SimpleConsole(IOutputBase):
    def print(self, autos):
        for auto in autos:
            print(auto)