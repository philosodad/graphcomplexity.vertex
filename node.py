import SimPy.Simulation as sim
import random as ran
import scipy as sci
import cove as cov
from obal import G as G
import bild as bil

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
        self.on = False

    def run(self):
        print self.id, [a.id for a in self.targets], [a.id for a in self.neighbors]
        yield sim.hold, self, self.battery_life
        print sim.now()
        print ("node %s died at %d" % (self.id, sim.now()))

    def build_covers(self):
        if len(self.targets) > 0:
            bil.init_covers(self)
            bil.update_degree(self)
            bil.update_lifetime(self)
            bil.update_on(self)
            self.covers.sort()

    def get_cover(self, x):
        for a in self.covers:
            if x == a.node_list:
                return a
        return None
