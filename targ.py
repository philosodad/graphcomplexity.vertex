import SimPy.Simulation as sim
import random as ran
import scipy as sci
from obal import G as G

class Target(object):
    Next_id = 0
    def __init__(self):
        self.x = ran.random() * G.bound
        self.y = ran.random() * G.bound
        self.id = Target.Next_id
        Target.Next_id += 1
