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
import caut as cau
import tast as tas
import edst as eds
from obal import G as G

class NodeSource(sim.Process):
    Next_id = 0
    def __init__(self):
        sim.Process.__init__(self, name="nodesource"+str(NodeSource.Next_id))
        self.id = NodeSource.Next_id
        self.nodes = []
        self.targets = []
        self.source_out = open("source.dat", 'w')
        NodeSource.Next_id += 1
        
    def generate(self, many, targs):
        for i in xrange(many):
            n = nod.Node(self)
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

    def feed(self, other):
        for i in self.nodes:
            n = (i.dup())
            sim.activate(n, n.run())
            other.nodes.append(n)
        eds.set_neighborhood(other)
        eds.set_targets(other)
        for a in other.nodes:
            a.build_covers()
        for a in other.nodes:
            for b in a.neighbors:
                aut.automata(b, a.id)
        
    def feed_nect(self, other):
        for i in self.nodes:
            n = (i.make_ctn(other))
            sim.activate(n, n.run())
            other.nodes.append(n)
        eds.set_neighborhood(other)
        eds.set_targets(other)
        for a in other.nodes:
            cau.t_algorithm(a)

    def output(self, time):
        x = len(self.targets)
        y = len(filter(lambda a: a.covered, self.targets))
        self.source_out.writelines("%d: %d targets, %d covered\n" %(time,x,y))
