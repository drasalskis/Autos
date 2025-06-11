from dataclasses import dataclass, field

@dataclass
class CarFilter:
    make: str | None
    model: str | None
    color: str | None
    year_from: int
    year_to: int
    price_from: float
    price_to: float

    def __post_init__(self):
        self.make = self.__add_wildcards(self.make)
        self.model = self.__add_wildcards(self.model)
        self.color = self.__add_wildcards(self.color)
    
    def __add_wildcards(self, value):
        return value if value is None else f"%{value}%"
