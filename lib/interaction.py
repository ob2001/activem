from itertools import combinations, permutations
from random import sample
from numpy.linalg import inv
from scipy.optimize import minimize_scalar

from .bot.bot import Bot

from .fs import np, distance, vecdiffr

# Returns the angle between two vectors
def angle(r1: np.ndarray, r2: np.ndarray) -> float:
    return np.arccos(r1@r2/np.sqrt(r1@r1*r2@r2))

# Returns True if point is in vision cone
# Returns False otherwise
def sees(r1: np.ndarray, u1: np.ndarray, thetavis: float, r2: np.ndarray) -> bool:
    phi = angle(u1 - r1, r2 - r1)
    return True if phi < thetavis else False

class InteractionMethods:
    # Intentionally does nothing. Will skip collision checking from swarm
    @staticmethod
    def nocollision(botlist):
        pass

    # Handles collision for a list of circles.
    # Checks whether each pair of circles is within collision
    # radius and moves them if so. Incorrect behaviour when
    # more than 2 bots collide simultaneously
    @staticmethod
    def ccollide(botlist):
        collang = np.pi
        botlist = sample(botlist, len(botlist))
        for _ in range(10):
            for bota, botb in combinations(botlist, 2):
                d = distance(bota.pos, botb.pos)
                if(d < (bota.r + botb.r) and angle(bota.uvec, vecdiffr(bota.pos, botb.pos, 1)) < collang and sees(bota.pos, bota.uvec, collang, botb.pos)):
                    vec = vecdiffr(bota.pos, botb.pos, (bota.r + botb.r - d)/2)
                    botb.pos += vec
                    bota.pos -= vec
                    bota.colliding = True
                    botb.colliding = True

    # Collision detector for a given botlist.
    # Returns a list of sets of colliding circle bots.
    # To be used in ccollidemulti for groups of more
    # than 2 bots colliding.
    @staticmethod
    def getccollisions(botlist) -> tuple[bool, list[Bot]]:
        collang = np.pi
        
        coll_list = [[i] + [j for j in range(i + 1, len(botlist)) if distance(botlist[i].pos, botlist[j].pos) < (botlist[i].r + botlist[j].r) and angle(botlist[i].uvec, vecdiffr(botlist[i].pos, botlist[j].pos, 1)) < collang and sees(botlist[i].pos, botlist[i].uvec, collang, botlist[j].pos)] for i in range(len(botlist))]

        coll_groups = [set(i) for i in coll_list if len(i) > 1]
        return coll_groups

    @staticmethod
    def ccollidemulti(botlist):
        pass

    # Handles collision for a list of ellipse bots.
    # Calls getellcollisions() for each unique pair of ellipses.
    def ellcollide(botlist):
        for bota, botb in combinations(botlist, 2):
            coll = InteractionMethods.getellcollisions(bota, botb)
            if coll:
                dr = vecdiffr(bota.pos, botb.pos, bota.b + botb.b - distance(bota.pos, botb.pos))
                bota.pos += dr
                botb.pos -= dr
            if not bota.colliding:
                bota.colliding = coll
            if not botb.colliding:
                botb.colliding = coll

    # Collision detector for a pair of ellipses.
    # Minimizes Kf for given pair of ellipses to determine whether
    # they collide
    @staticmethod
    def getellcollisions(botA: Bot, botB: Bot) -> bool:
        a, A = botA.pos, botA.getA()
        b, B = botB.pos, botB.getA()
        res = minimize_scalar(InteractionMethods.Kf, bracket = [0.001, 0.5, 0.999], args = (a, b, A, B))
        return res.fun >= 0.7

    # Function used in ellipse collision test.
    # If the minimum of this function for s between 0 and 1 is
    # greater than 0, the ellipses collide
    @staticmethod
    def Kf(s: float, a: np.ndarray, b: np.ndarray, A: np.ndarray, B: np.ndarray) -> float:
        return 1 - (b - a).T@inv(inv(A)/(1-s)+inv(B)/s)@(b - a)

    @staticmethod
    def vicsekflock(botlist):
        pass

    @staticmethod
    def gencollide(botlist):
        """Most general collider. Can be used for swarms with different types of bots."""
        pass