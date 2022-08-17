from abc import ABC, abstractmethod

from ..lib import np, rotvec, randbw, uvecfromang

class Bot(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def draw(self, ax):
        """Method used to draw bot shape at correct position and with correct orientation, size, etc"""
        pass

    @abstractmethod
    def redraw(self, shape):
        pass

    # Rotate uvec by angle specified.
    def rotate(self, theta):
        self.uvec = rotvec(self.uvec, theta)
        self.normalizeuvec()

    # Renormalizes bot's uvec
    def normalizeuvec(self):
        self.uvec = self.uvec/np.linalg.norm(self.uvec)

    def randpos(self, w, h):
        self.pos = [randbw(w), randbw(h)]

    def randuvec(self):
        self.uvec = uvecfromang(randbw(np.pi))
        self.normalizeuvec()
