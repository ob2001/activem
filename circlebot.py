from lib import *
from bot import Bot

# Class for each individual bot. Each one will have
# access to its own position, direction, etc.
class CircleBot(Bot):
    v = 0.08
    collrad = 1.5
    collang = np.pi

    def __init__(self, W, H, p_res, d_res):
        self.pos = [randbw(W, p_res), randbw(H, p_res)]
        self.uvec = [randbw(1, d_res), randbw(1, d_res)]

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

    def collision(self, botb):
        d = distance(self.pos, botb.pos)
        if(d < self.collrad and angle(self.uvec, vecdiffr(self.pos, botb.pos, 1)) < self.collang and sees(self.pos, self.uvec, self.collang, botb.pos)[0]):
            vec = vecdiffr(self.pos, botb.pos, (self.collrad - d)/2)
            botb.pos += vec
            self.pos -= vec