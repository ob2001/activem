from abc import ABC, abstractmethod

# Class for the arena in which the bots are interacting.
class Arena(ABC):
    # TODO: Boundary types:
    # TODO - Solid
    # Done - Periodic
    # DONE - Reflective

    # TODO: Boundary shapes:
    # TODO - Circular
    # Done - Rectangular

    @abstractmethod
    def boundsup(self):
        pass

    @abstractmethod
    def boundcoll(self, items):
        pass