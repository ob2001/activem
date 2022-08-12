from lib import *
from abc import ABC, abstractmethod

class Bot(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def rotate(self, theta: float):
        pass

    @abstractmethod
    def draw():
        """Method used to draw bot shape at correct position and with correct orientation, size, etc"""
        pass