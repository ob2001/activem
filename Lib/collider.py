from .lib import np, distance, vecdiffr

class Collider():
    def ccollide(botlist):
        collang = np.pi
        for i in range(len(botlist)):
            for j in range(len(botlist)):
                if(i == j):
                    continue
                else:
                    obj1, obj2 = botlist[i], botlist[j]
                    d = distance(obj1.pos, obj2.pos)
                    if(d < obj1.r and angle(obj1.uvec, vecdiffr(obj1.pos, obj2.pos, 1)) < collang and sees(obj1.pos, obj1.uvec, collang, obj2.pos)[0]):
                        vec = vecdiffr(obj1.pos, obj2.pos, (obj1.r - d)/2)
                        obj2.pos += vec
                        obj1.pos -= vec

    def ccollidemulti(botlist):
        pass

# Returns the angle between two vectors
def angle(r1, r2):
    return np.arccos(r1@r2/np.sqrt(r1@r1*r2@r2))

# Returns True if point is in vision cone
# Returns False otherwise
def sees(r1, u1, thetavis, r2):
    phi = angle(u1 - r1, r2 - r1)
    return [True, phi] if phi < thetavis else [False, 0.]