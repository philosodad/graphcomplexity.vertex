#node.py
#paul daigle
#Class file that contains the main process (sensor nodes) and logic for the simulation

import random as ran
import scipy as sci
import ctno as ctn
import copy
import neco as cov
from obal import G as G
import bedg as bil
import auto as aut

class Node(object):
    Next_id = 0
    def __init__(self, parent):
        self.id = Node.Next_id
        self.battery_life = ran.randint(140,150)
        Node.Next_id += 1
        self.x = ran.random() * G.bound
        self.y = ran.random() * G.bound
        self.targets = []
        self.neighbors = []
        self.covers = []
        self.on = True
        self.current_cover = None
        self.current_cover_index = 0
        self.parent = parent

    def __cmp__(self, other):
        if self.battery_life < other.battery_life:
            return -1
        elif self.battery_life > other.battery_life:
            return 1
        else:
            return 0

    def dup(self, parent):
        n = Node(parent)
        n.x = self.x
        n.y = self.y
        n.battery_life = self.battery_life
        return n
    
    def make_ctn(self, parent):
        n = ctn.T_Node(parent)
        n.x = self.x
        n.y = self.y
        n.battery_life = self.battery_life
        return n

    def build_covers(self):
        if len(self.targets) > 0:
            bil.init_covers(self)
            bil.update_degree(self)
            bil.update_lifetime(self)
            bil.update_on(self)
            self.covers.sort()
            self.current_cover_index = 0
            self.current_cover = self.covers[0]
        else:
            self.on = False

    def update_covers(self):
        for a in filter(lambda a: a.battery_life == 0, self.neighbors):
            self.covers = filter(lambda b: a.id not in b.node_list, self.covers)
        if self.battery_life == 0:
            self.covers = filter(lambda b: self.id not in b.node_list, self.covers)
        bil.update_degree(self)
        bil.update_lifetime(self)
        bil.update_on(self)
        self.covers.sort()

    def get_cover(self, x):
        for a in self.covers:
            if x == a.node_list:
                return a
        return None


            
