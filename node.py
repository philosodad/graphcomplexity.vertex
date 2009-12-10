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
        self.targets = []
        self.neighbors = []
        self.covers = []

    def run(self):
        print self.id, [a.id for a in self.targets], [a.id for a in self.neighbors]
        yield sim.hold, self, self.battery_life
        print sim.now()
        print ("node %s died at %d" % (self.id, sim.now()))

    def build_covers(self):
        big_list = {}
        big_list = big_list.fromkeys(self.targets)
        for a in big_list:
            big_list[a] = [self.id]

        for a in self.neighbors:
            for b in big_list.keys():
                if b in a.targets:
                    big_list[b].append(a.id)
        
        small_list = big_list.values()
        slots = 1
        for a in small_list:
            slots = slots * len(a)
        c = []
        for i in range(slots):
            c.append([])
        b = 1
        for i in range(len(small_list)):
            g = 0
            f = 0
            while g < len(c):
                for j in range(b):
                    c[g].append(small_list[i][f%len(small_list[i])])
                    g+=1
                f+=1
            b = b * len(small_list[i])
            
        for a in c:
            self.covers.append(cov.Cover(set(a)))
            
        keyed_lifetimes = {}
        keyed_lifetimes[self.id] =  self.battery_life
        for a in self.neighbors:
            keyed_lifetimes[a.id] = a.battery_life
        for a in self.covers:
            lives = []
            for b in a.node_list:
                lives.append(keyed_lifetimes[b])
            lives.sort()
            a.lifetime = lives.pop()
        return big_list

    def get_cover(self, x):
        for a in self.covers:
            if x == a.node_list:
                return a
        return None
