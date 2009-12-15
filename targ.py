import random as ran
from obal import G as G

class Target(object):
    Next_id = 0
    def __init__(self):
        self.x = ran.random() * G.bound
        self.y = ran.random() * G.bound
        self.uv = set([])
        self.id = Target.Next_id
        Target.Next_id += 1
