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
import edst as eds
from obal import G as G

class NodeSource(sim.Process):
    nodes = []
    targets = []
    Next_id = 0
    def __init__(self):
        sim.Process.__init__(self, name="nodesource"+str(NodeSource.Next_id))
        NodeSource.Next_id += 1
        
    def generate(self, many, targs):
        for i in xrange(many):
            n = nod.Node()
            sim.activate(n, n.run()) 
            self.nodes.append(n)
        eds.populate_targets(self, targs)
        eds.set_neighborhood(self)
        eds.set_targets(self)
        for a in self.nodes:
            a.build_covers()
        for a in self.nodes:
            for b in a.neighbors:
                aut.automata(b, a.id)
