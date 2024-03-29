from abc import ABC, abstractmethod
from matplotlib.pyplot import Axes

# Class for the arena in which the bots are interacting.
class Arena(ABC):
    # TODO: Boundary types:
    # Done - Solid
    # Done - Periodic
    # Done - Reflective

    # TODO: Boundary shapes:
    # TODO - Circular
    # Done - Rectangular

    @abstractmethod
    def boundsup(self):
        pass

    @abstractmethod
    def boundcoll(self, items: list):
        pass

    # Randomizes an object's position within arena bounds
    @abstractmethod
    def randpos(self, bot):
        pass