#node.py
#paul daigle
#Class file that contains the main process (sensor nodes) and logic for the simulation

import SimPy.SimulationTrace as sim
import random as ran
import scipy as sci
import cove as cov
from obal import G as G
import bild as bil
import auto as aut

class Node(sim.Process):
    Next_id = 0
    def __init__(self):
        sim.Process.__init__(self, name="node"+str(Node.Next_id))
        self.id = Node.Next_id
        self.battery_life = ran.randint(100,150)
        Node.Next_id += 1
        self.x = ran.random() * G.bound
        self.y = ran.random() * G.bound
        self.targets = []
        self.neighbors = []
        self.covers = []
        self.on = True
        self.current_cover = None
        self.current_cover_index = 0

    def run(self):
        
        while 1:
            print self.id, self.battery_life, self.on, [a.id for a in self.targets], [a.id for a in self.neighbors]
            now = sim.now()
            if self.on:
                yield sim.hold, self, self.battery_life
                self.battery_life = 0
                self.on = False
                for a in self.neighbors:
                    if not a.on:
                        a.update_covers
                        aut.automata(a, self.id)
                        if a.on:
                            sim.reactivate(a)
                print ("node %s died at %d" % (self.id, sim.now()))
            else:
                yield sim.passivate, self

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
        bil.update_degree(self)
        bil.update_lifetime(self)
        bil.update_on(self)
        self.covers.sort()

    def get_cover(self, x):
        for a in self.covers:
            if x == a.node_list:
                return a
        return None


            
