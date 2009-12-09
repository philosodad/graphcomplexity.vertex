import SimPy.Simulation as sim
import random as ran
import scipy as sci
import cove as cov
from obal import G as G

class Node(sim.Process):
    Next_id = 0
    def __init__(self):
        sim.Process.__init__(self, name="node"+str(Node.Next_id))
        self.id = Node.Next_id
        self.battery_life = ran.randint(100,150)
        Node.Next_id += 1
        self.x = ran.random() * G.bound
        self.y = ran.random() * G.bound
        self.targets = {}
        self.neighbors = {}
        self.covers = {}

    def run(self):
        print sim.now(), self
        yield sim.hold, self, self.battery_life
        print ("node %s died at %d" % (self.id, sim.now()))

    def build_covers(self):
        big_list = {}
        big_list = big_list.fromkeys(self.targets.keys())
        for a in big_list:
            big_list[a] = [self.id]

        for a in self.neighbors:
            for b in big_list.keys():
                if b in self.neighbors[a].targets.keys():
                    big_list[b].append(a)
        return big_list
