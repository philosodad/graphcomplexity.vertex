#ctno.py
#paul daigle
#Class file that contains the cover 2 (sensor nodes) and logic for the simulation

#import SimPy.SimulationTrace as sim
import SimPy.Simulation as sim
#import SimPy.SimulationStep as sim
import random as ran
import scipy as sci
import copy
import cove as cov
import geom as geo
from obal import G as G
import bild as bil
import caut as cau

class T_Node(object):
    Next_id = 0
    def __init__(self, parent):
        self.id = T_Node.Next_id
        self.battery_life = ran.randint(100,150)
        T_Node.Next_id += 1
        self.x = ran.random() * G.bound
        self.y = ran.random() * G.bound
        self.targets = []
        self.neighbors = []
        self.covers = []
        self.on = False
        self.root = False
        self.active = False
        self.ex = 0
        self.current_cover = None
        self.current_cover_index = 0
        self.parent = parent

    def dup(self):
        n = T_Node()
        n.x = self.x
        n.y = self.y
        n.battery_life = self.battery_life
        return n

    def __cmp__(self, other):
        if self.battery_life < other.battery_life:
            return -1
        elif self.battery_life > other.battery_life:
            return 1
        else:
            return 0

