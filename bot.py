from lib import *

# Class for each individual bot. Each one will have
# access to its own position, direction, etc.
class Bot:
    v = 0.08

    def __init__(self, pos, uvec, arena, xbound, ybound):
        self.pos = pos
        self.uvec = uvec
        self.xbound, self.ybound = xbound, ybound
        self.arena = arena

        self.normalizeuvec()

    # Renormalizes bot's uvec
    def normalizeuvec(self):
        self.uvec = self.uvec/np.linalg.norm(self.uvec)

    # Rotate uvec directly via its x and y coordinates
    # rather than providing an angle to rotate by
    def rotatecart(self, x, y):
        self.uvec += [x, y]
        self.normalizeuvec()

    # Rotate uvec by angle specified.
    def rotate(self, theta, r):
        self.uvec += [r*np.cos(theta), r*np.sin(theta)]
        self.normalizeuvec()