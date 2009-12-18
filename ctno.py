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

class T_Node(sim.Process):
    Next_id = 0
    def __init__(self, parent):
        sim.Process.__init__(self, name="t-node"+str(T_Node.Next_id))
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

    def run(self):
        while 1:
            cau.t_algorithm(self)
            print "time: ", sim.now(), "t_node: ", self.id, self.battery_life, self.on, [a.uv for a in self.targets], [a.id for a in self.neighbors]
            now = sim.now()
            if self.on:
                k = geo.key_targets(self)
                for a in self.neighbors:
                    k[a.id].covered = True
                print "t_node: ", self.id
                yield sim.hold, self, self.battery_life
                self.battery_life = 0
                self.parent.output(sim.now())
                self.on = False
                self.ex = 0
                for a in self.neighbors:
                    if not a.on:
                        k[a.id].covered = False
                        k[a.id].active = False
                        k[a.id].star_edge = False
                for a in self.neighbors:
                    if a.battery_life > 0:
                        sim.reactivate(a)
                        cau.t_algorithm(a)
                print ("t_node %s died at %d" % (self.id, sim.now()))
            else:
                yield sim.passivate, self
