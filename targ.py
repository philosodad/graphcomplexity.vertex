import random as ran
from obal import G as G

class Target(object):
    Next_id = 0
    def __init__(self):
        self.uv = set([])
        self.id = Target.Next_id
        self.keyed_uv = {}
        self.weight = 0
        self.covered = False
        Target.Next_id += 1

    def dup(self):
        t = Target()
        t.x = self.x
        t.y = self.y
        return t
