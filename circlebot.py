from lib import *
from bot import Bot

# Class for each individual bot. Each one will have
# access to its own position, direction, etc.
class CircleBot(Bot):
    v = 0.8
    collrad = 4.0
    collang = np.pi
    name = "CircleBot"

    def __init__(self, W, H, kwargs, p_res = 100, d_res = 100):
        self.pos = [randbw(W, p_res), randbw(H, p_res)]
        self.uvec = [randbw(1, d_res), randbw(1, d_res)]
        self.normalizeuvec()

    # Renormalizes bot's uvec
    def normalizeuvec(self):
        self.uvec = self.uvec/np.linalg.norm(self.uvec)

    # Rotate uvec by angle specified.
    def rotate(self, theta):
        self.uvec = rotvec(self.uvec, theta)
        self.normalizeuvec()

    def collision(self, botb):
        d = distance(self.pos, botb.pos)
        if(d < self.collrad and angle(self.uvec, vecdiffr(self.pos, botb.pos, 1)) < self.collang and sees(self.pos, self.uvec, self.collang, botb.pos)[0]):
            vec = vecdiffr(self.pos, botb.pos, (self.collrad - d)/2)
            botb.pos += vec
            self.pos -= vec

    def draw(self, ax):
        ax.add_patch(plt.Circle((self.pos[0], self.pos[1]), self.collrad/2, fill = False, edgecolor = 'black'))