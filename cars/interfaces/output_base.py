from abc import ABC, abstractmethod
from typing import List

from cars.models import Auto


class IOutputBase(ABC):
    @abstractmethod
    def print(self, autos: List[Auto]):
        pass