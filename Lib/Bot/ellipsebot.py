from ..lib import np, randbw, rotvec, angfromuvecd
from .bot import Bot
from matplotlib.patches import Ellipse

class EllipseBot(Bot):
    v = 0.08
    name = "EllipseBot"

    def __init__(self, W, H, kwargs):
        a, b = kwargs['a'], kwargs['b']
        self.pos = np.array([randbw(W), randbw(H)])
        self.uvec = np.array([randbw(1), randbw(1)]) # Points in direction of major axis
        self.normalizeuvec()
        if(a is None and b is None):
            self.a, self.b = randbw(1), randbw(1)
        elif(a is not None and b is not None):
            self.a, self.b = a, b
        elif(a is not None):
            self.a, self.b = a, randbw(1)
        else:
            self.a, self.b = randbw(1), b

    # Get bot's ovec
    def getovec(self):
        return rotvec(self.uvec, -np.pi/2)

    def collision(self, botb):
        pass

    def draw(self, ax):
        ax.add_patch(Ellipse((self.pos[0], self.pos[1]), self.a, self.b, fill = False, angle = 90 + angfromuvecd(self.uvec)))