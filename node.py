import SimPy.Simulation as sim
import random as ran
import scipy as sci
import glob

class Node(sim.Process):
    Next_id = 0
    def __init__(self):
        sim.Process.__init__(self, name="node"+str(Node.Next_id))
        self.id = Node.Next_id
        self.battery_life = ran.randint(100,150)
        Node.Next_id += 1
        self.x_coord = ran.rand() * glo.bound

    def run(self):
        print sim.now(), self
        yield sim.hold, self, self.battery_life
        print ("node %s died at %d" % (self.id, sim.now()))
