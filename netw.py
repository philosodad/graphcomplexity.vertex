import SimPy.Simulation as sim
import random as ran
import scipy as sci
import node as nod

class NodeSource(sim.Process):
    def generate(self, many):
        for i in xrange(many):
            n = nod.Node()
            sim.activate(n, n.run()) 
