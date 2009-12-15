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
import tast as tas
from obal import G as G

class NodeSource(object):
    nodes = []
    targets = []
    def generate(self, many, targs):
        for i in xrange(many):
            n = nod.Node()
            sim.activate(n, n.run()) 
            self.nodes.append(n)
        tas.populate_targets(self, targs)
        tas.set_targets(self)
        tas.set_neighborhood(self)
        for a in self.nodes:
            a.build_covers()
        for a in self.nodes:
            for b in a.neighbors:
                aut.automata(b, a.id)
        
