import geom as geo
import targ as tar
from obal import G as G

def populate_targets(net, targs):
    for i in xrange(targs):
        t = tar.Target()
        net.targets.append(t)

def set_targets(net):
    for i in net.nodes:
        for j in net.targets:
            if geo.dist(i, j) < G.sensor_range:
                i.targets.append(j)

def set_neighborhood(net):
    for i in net.nodes:
        for j in net.nodes:
            if j != i:
                if geo.dist(i,j) < G.comm_range:
                    i.neighbors.append(j)
