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
from obal import G as G

class NodeSource(object):
    Next_id = 0
    def __init__(self):
        self.id = NodeSource.Next_id
        self.nodes = []
        self.targets = []
        self.keyed_nodes = {}
        self.approx = 0
        NodeSource.Next_id += 1
        
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
            if targs > (len(self.nodes)*.5)*(len(self.nodes)-1):
                targs = (len(self.nodes)*.5)*(len(self.nodes)-1)
                print "but now targs is equal to ", targs
            den.set_neighborhood(self, targs)
            den.set_targets(self)
        self.approx = seq.sequential(self)
        for a in self.targets:
            a.keyed_uv[a.id] = a.uv
        for a in self.nodes:
            self.keyed_nodes[a.id] = a
        for a in self.nodes:
            a.build_covers()

    def generate_alt(self, many, targs):
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
            if targs > (len(self.nodes)*.5)*(len(self.nodes)-1):
                targs = (len(self.nodes)*.5)*(len(self.nodes)-1)
                print "but now targs is equal to ", targs
            den.set_neighborhood(self, targs)
            den.set_targets(self)
        self.approx = seq.sequential(self)
        for a in self.targets:
            a.keyed_uv[a.id] = a.uv
        for a in self.nodes:
            self.keyed_nodes[a.id] = a
        for a in self.nodes:
            a.build_neg_covers()
            

    def once(self):
        for a in self.nodes:
            for b in a.neighbors:
                aut.automata(a, b.id)

    def go(self):
        time = 0
#        for a in self.nodes:
#            print "node: ", a.id, a.battery_life, a.on, [b.node_list for b in a.covers], [b.uv for b in a.targets], [b.id for b in a.neighbors]
        for a in self.nodes:
            for b in a.neighbors:
                aut.automata(a, b.id)
        first = len( filter(lambda a: a.on, self.nodes))
        if self.targets:
            while(self.targets_covered()):
                self.nodes.sort()
                current_node = filter(lambda a: a.on, self.nodes)[0]
                time = time + current_node.battery_life
    #            print "a_time: ", time, "cover: ", [a.id for a in filter(lambda b: b.on, self.nodes)]
                current_node.on = False
                for a in filter(lambda a: a.on, self.nodes):
                    a.battery_life = a.battery_life - current_node.battery_life
                current_node.battery_life = 0
                for a in current_node.neighbors:
                    aut.automata(a, current_node.id)
        return first, time
                
            
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
            
