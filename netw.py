import SimPy.Simulation as sim
import random as ran
import scipy as sci
import node as nod
import targ as tar
import geom as geo
from obal import G as G

class NodeSource(sim.Process):
    nodes = []
    targets = []
    def generate(self, many, targs):
        for i in xrange(many):
            n = nod.Node()
            sim.activate(n, n.run()) 
            self.nodes.append(n)
        for i in xrange(targs):
            t = tar.Target()
            self.targets.append(t)
        self.set_targets()
        for a in self.nodes:
            a.build_covers()
        

    def set_targets(self):
        for i in self.nodes:
            for j in self.targets:
                if geo.dist(i, j) < G.sensor_range:
                    i.targets.append(j)

    def set_neighborhood(self):
        for i in self.nodes:
            for j in self.nodes:
                if j != i:
                    if j not in i.neighbors and geo.dist(i,j) < G.comm_range:
                        i.neighbors.append(j)
                        j.neighbors.append(i)
