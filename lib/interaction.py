import random

from .fs import np, distance, vecdiffr

# Returns the angle between two vectors
def angle(r1, r2):
    return np.arccos(r1@r2/np.sqrt(r1@r1*r2@r2))

# Returns True if point is in vision cone
# Returns False otherwise
def sees(r1, u1, thetavis, r2):
    phi = angle(u1 - r1, r2 - r1)
    return True if phi < thetavis else False

class InteractionMethods:
    @staticmethod
    def nocollision(botlist):
        """Intentionally empty. Will skip collision checking from swarm"""
        pass

    @staticmethod
    def ccollide(botlist):
        collang = np.pi
        botlist = random.sample(botlist, len(botlist))
        for i in range(len(botlist)):
            for j in range(len(botlist)):
                if(i == j):
                    continue
                else:
                    obj1, obj2 = botlist[i], botlist[j]
                    d = distance(obj1.pos, obj2.pos)
                    if(d < (obj1.r + obj2.r) and angle(obj1.uvec, vecdiffr(obj1.pos, obj2.pos, 1)) < collang and sees(obj1.pos, obj1.uvec, collang, obj2.pos)):
                        vec = vecdiffr(obj1.pos, obj2.pos, (obj1.r + obj2.r - d)/2)
                        obj2.pos += vec
                        obj1.pos -= vec

    @staticmethod
    def getccollisions(botlist):
        collang = np.pi
        
        coll_list = [[i] + [j for j in range(i + 1, len(botlist)) if distance(botlist[i].pos, botlist[j].pos) < (botlist[i].r + botlist[j].r) and angle(botlist[i].uvec, vecdiffr(botlist[i].pos, botlist[j].pos, 1)) < collang and sees(botlist[i].pos, botlist[i].uvec, collang, botlist[j].pos)] for i in range(len(botlist))]

        coll_groups = [i for i in coll_list if len(i) > 1]
        return coll_groups

    @staticmethod
    def ccollidemulti(botlist):
        colls = InteractionMethods.getccollisions(botlist)
        pass

    def ellcollide(botlist):
        pass

    @staticmethod
    def vicsekflock(botlist):
        pass

    @staticmethod
    def gencollide(botlist):
        """Most general collider. Can be used for swarms with different types of bots."""
        pass