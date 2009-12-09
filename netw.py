import SimPy.Simulation as sim
import random as ran
import scipy as sci
import node as nod
import targ as tar
import geom as geo
from obal import G as G

class NodeSource(sim.Process):
    network = {'nodes':{}, 'targets':{}}
    def generate(self, many, targs):
        for i in xrange(many):
            n = nod.Node()
            sim.activate(n, n.run()) 
            self.network['nodes'][n.id]=n
        for i in xrange(targs):
            t = tar.Target()
            self.network['targets'][t.id]=n
        self.set_targets()
        

    def set_targets(self):
        for i in self.network['nodes']:
            no = self.network['nodes'][i]
            for j in self.network['targets']:
                ta = self.network['targets'][j]
                if geo.dist(no, ta) < G.sensor_range:
                    no.targets[j] = ta

    def set_neighborhood(self):
        for i in self.network['nodes']:
            no = self.network['nodes'][i]
            for j in self.network['nodes']:
                if j != i:
                    de = self.network['nodes'][j]
                    if de not in no.neighbors and geo.dist(no,de) < G.comm_range:
                        no.neighbors[j] = de
                        de.neighbors[i] = no
