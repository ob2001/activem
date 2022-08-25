from abc import ABC, abstractmethod

from ..fs import np, rotvec, randbw, uvecfromang

class Bot(ABC):
    @abstractmethod
    def __init__(self):
        pass

    # Method used to draw bot shape at correct position
    # and with correct orientation, size, etc
    @abstractmethod
    def draw(self, ax):
        pass

    # Method called when drawing animation to update
    # bot's plot element(s)
    @abstractmethod
    def redraw(self, shape):
        pass

    # Rotate uvec by angle specified.
    def rotate(self, theta):
        self.uvec = rotvec(self.uvec, theta)
        self.normalizeuvec()

    # Renormalizes a bot's uvec
    def normalizeuvec(self):
        self.uvec = self.uvec/np.linalg.norm(self.uvec)

    # Randomizes bot's position within given bounds
    def randpos(self, w, h):
        self.pos = np.array([randbw(w), randbw(h)])

    # Randomizes bot's orientation (ovec)
    def randuvec(self):
        self.uvec = uvecfromang(randbw(np.pi))
        self.normalizeuvec()
