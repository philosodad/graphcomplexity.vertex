import geom as geo
import targ as tar
from obal import G as G

def populate_targets(net, targs):
    pass


def set_neighborhood(net):
    def add_edge(i,j):
        t = tar.Target()
        t.uv = set([i.id, j.id])
        net.targets.append(t)

    for i in net.nodes:
        for j in net.nodes:
            if j != i:
                if geo.dist(i,j) < G.comm_range:
                    i.neighbors.append(j)
                    if net.targets:
                        if set([i.id, j.id]) not in [a.uv for a in net.targets]:
                            add_edge(i,j)
                    else:
                        add_edge(i,j)
                            

def set_targets(net):
    for i in net.nodes:
        for t in net.targets:
            if i.id in t.uv:
                if t not in i.targets:
                    i.targets.append(t)
            
            
                            
