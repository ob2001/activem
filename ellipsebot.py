from lib import *
from bot import Bot

class EllipseBot(Bot):
    v = 0.08
    def __init__(self, W, H, p_res, d_res):
        self.pos = np.array([randbw(W, p_res), randbw(H, p_res)])
        self.uvec = np.array([randbw(1, d_res), randbw(1, d_res)]) # Points in direction of major axis
        self.normalizeuvec()
        self.a, self.b = randbw(1, d_res), randbw(1, d_res)

    # Renormalizes bot's uvec
    def normalizeuvec(self):
        self.uvec = self.uvec/np.linalg.norm(self.uvec)

    # Get bot's ovec
    def getovec(self):
        return rotvec(-np.pi/2)@self.uvec

    def collision(self, botb):
        pass