#netw.py
#j.paul daigle
#generation and data structure for the network as a whole. 

import SimPy.Simulation as sim
import random as ran
import scipy as sci
import node as nod
import targ as tar
import geom as geo
import auto as aut
from obal import G as G

class NodeSource(object):
    nodes = []
    targets = []
    def generate(self, many, targs):
        for i in xrange(many):
            n = nod.Node()
            sim.activate(n, n.run()) 
            self.nodes.append(n)
        # Target constructor should be abstracted from this class to allow different algorithms, target coverage, area coverage, etc.
        for i in xrange(targs):
            t = tar.Target()
            self.targets.append(t)
        self.set_targets()
        self.set_neighborhood()
        for a in self.nodes:
            a.build_covers()
        for a in self.nodes:
            for b in a.neighbors:
                aut.automata(b, a.id)
        
    #these should be imported from another file, again for system flexibility            
    def set_targets(self):
        for i in self.nodes:
            for j in self.targets:
                if geo.dist(i, j) < G.sensor_range:
                    i.targets.append(j)

    def set_neighborhood(self):
        for i in self.nodes:
            for j in self.nodes:
                if j != i:
                    if geo.dist(i,j) < G.comm_range:
                        i.neighbors.append(j)
