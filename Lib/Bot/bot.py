from abc import ABC, abstractmethod

from ..lib import np, rotvec

class Bot(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def collision(self, botb):
        pass

    @abstractmethod
    def draw(ax):
        """Method used to draw bot shape at correct position and with correct orientation, size, etc"""
        pass

    # Rotate uvec by angle specified.
    def rotate(self, theta):
        self.uvec = rotvec(self.uvec, theta)
        self.normalizeuvec()

    # Renormalizes bot's uvec
    def normalizeuvec(self):
        self.uvec = self.uvec/np.linalg.norm(self.uvec)
