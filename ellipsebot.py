from lib import *
from bot import Bot
from matplotlib.patches import Ellipse

class EllipseBot(Bot):
    v = 0.08
    name = "EllipseBot"

    def __init__(self, W, H, p_res, d_res, a = None, b = None):
        self.pos = np.array([randbw(W, p_res), randbw(H, p_res)])
        self.uvec = np.array([randbw(1, d_res), randbw(1, d_res)]) # Points in direction of major axis
        self.normalizeuvec()
        if(a is None and b is None):
            self.a, self.b = randbw(1, d_res), randbw(1, d_res)
        elif(a is not None and b is not None):
            self.a, self.b = a, b
        elif(a is not None):
            self.a, self.b = a, randbw(1, d_res)
        else:
            self.a, self.b = randbw(1, d_res), b

    # Renormalizes bot's uvec
    def normalizeuvec(self):
        self.uvec = self.uvec/np.linalg.norm(self.uvec)

    def rotate(self, theta):
        self.uvec = rotvec(self.uvec, theta)
        self.normalizeuvec()

    # Get bot's ovec
    def getovec(self):
        return rotvec(self.uvec, -np.pi/2)

    def collision(self, botb):
        pass

    def draw(self, ax):
        ax.add_patch(Ellipse((self.pos[0], self.pos[1]), self.a, self.b, angle = 90 + angfromuvecd(self.uvec)))