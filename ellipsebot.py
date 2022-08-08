from lib import *
from bot import Bot

class EllipseBot(Bot):
    def __init__(self, W, H, p_res, d_res):
        self.pos = [randbw(W, p_res), randbw(H, p_res)]
        self.uvec = [randbw(1, d_res), randbw(1, d_res)]
        self.a, self.b = a, b