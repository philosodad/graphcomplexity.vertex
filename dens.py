import geom as geo
import targ as tar
import random as ran
from obal import G as G

def populate_targets(net, targs):
    pass


def set_neighborhood(net, targs):
    print ("Let's set the neighborhood with %d!" %(targs))
    
    def add_edge(i,j):
        print "Let's add an edge"
        t = tar.Target()
        t.uv = set([i.id, j.id])
        net.targets.append(t)
        
    def make_target(i,j):
        print "Let's make a target!"
        if i.id != j.id:
            if net.targets:
                if set([i.id, j.id]) not in [a.uv for a in net.targets]:
                    i.neighbors.append(j)
                    j.neighbors.append(i)
                    add_edge(i,j)
            else:
                i.neighbors.append(j)
                j.neighbors.append(i)
                add_edge(i,j)                

    while len(net.targets) < targs:
        print ("net.targets is %d, which is less than %d!" %(len(net.targets), targs))
        if targs == (len(net.nodes) * (len(net.nodes)-1) * .5):
            for i in (net.nodes):
                for j in (net.nodes):
                    make_target(i,j)
        else:
            i = ran.choice(net.nodes)
            j = ran.choice(net.nodes)
            make_target(i,j)

                

def set_targets(net):
    print "let's set our targets"
    for i in net.nodes:
        for t in net.targets:
            if i.id in t.uv:
                if t not in i.targets:
                    i.targets.append(t)
    print "I'm done setting targets"
            
                            
