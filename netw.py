#netw.py
#j.paul daigle
#generation and data structure for the network as a whole. 
import random as ran
import node as nod
import targ as tar
import geom as geo
import auto as aut
import caut as cau
import tast as tas
import edst as eds
import sequ as seq
import dens as den
import nolp as nol
import dgmm as dgm
from obal import G as G

class NodeSource(object):
    Next_id = 0
    def __init__(self):
        self.id = NodeSource.Next_id
        self.nodes = []
        self.targets = []
        self.keyed_nodes = {}
        NodeSource.Next_id += 1
        

    def key(self):
        for a in self.targets:
            a.keyed_uv[a.id] = a.uv
        for a in self.nodes:
            self.keyed_nodes[a.id] = a

    def generate(self, many, targs):
        print "let's add ", many
        for i in xrange(many):
            n = nod.Node(self)
            self.nodes.append(n)
        if not targs:
            eds.populate_targets(self, targs)
            eds.set_neighborhood(self)
            eds.set_targets(self)
        else:
            print "targs is equal to ", targs
            print ("there are %d nodes" %(len(self.nodes)))
            if targs > .5*(len(self.nodes)*(len(self.nodes)-1)):
                targs = .5*(len(self.nodes)*(len(self.nodes)-1))
                print "but now targs is equal to ", targs
            den.set_neighborhood(self, targs)
            den.set_targets(self)
        self.key()
        for a in self.nodes:
            a.build_covers()            

    def seq(self):
        return seq.sequential(self)

    def weighted_seq(self):
        return nol.gmm(self)

    def weighted_dist(self):
        dgm.init(self)
        while not self.targets_covered():
            dgm.set_partners(self)
            dgm.set_edge(self)
        on_list = filter(lambda a: a.on, self.nodes)
        w = sum([b.battery_life for b in on_list])
        l = len(on_list)
        return l, w

    def once(self):
        for a in self.nodes:
            aut.automata(a)
        return len(filter(lambda a: a.on == True, self.nodes))

    def feed(self, other):
        for i in self.nodes:
            n = (i.dup(other))
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
            other.nodes.append(n)
        eds.set_neighborhood(other)
        eds.set_targets(other)

    def output(self, time):
        x = len(self.targets)
        y = len(filter(lambda a: a.covered, self.targets))
        self.source_out.writelines("%d: %d targets, %d covered\n" %(time,x,y))

    def targets_covered(self):
        on_list = set([b.id for b in filter(lambda a: a.on, self.nodes)])
        if len(self.targets) == 0:
            return False
        if len(on_list) == 0:
            return False
        for a in self.targets:
            if len(a.uv - on_list) == 2:
                return False
        return True

    def get_degree(self):
        degree = 0
        for a in self.nodes:
            degree = degree + len(a.neighbors)
        return degree/len(self.nodes)
            
