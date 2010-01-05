import random as ran
import copy as cop

def init(net):
    for a in net.targets:
        a.weight = -1
    for a in net.nodes:
        a.on = False
        a.weight = a.battery_life
        for b in a.neighbors:
            a.keyed_neighbors[b.id] = b

def set_partners(net):
    t_list = []
    for a in net.nodes:
        a.round_partner = None
    for a in net.targets:
        if a.weight == -1:
            t_list.append(a)
    if not t_list:
        return True #the graph is matched
    while t_list:
        e_list = []
        edge = ran.choice(t_list)
#        print "pulled ", edge.uv
        g = cop.copy(edge.uv)
        u = g.pop()
        v = g.pop()
        for a in t_list:
            if len(a.uv - edge.uv) == 2:
                e_list.append(a)
#                print "put %s in e_list" % a.uv
        t_list = e_list
        net.keyed_nodes[u].round_partner = v
        net.keyed_nodes[v].round_partner = u
#        print ("set %d's round partner to %d" %(v,u))
#        print ("set %d's round partner to %d" %(u,v))

def set_edge(net):
    for a in net.nodes:
        if not a.round_partner == None:
            print "%d has a round partner of %s" %(a.id, a.round_partner)

            b = net.keyed_nodes[a.round_partner]
            edgeuv = set([a.id, b.id])
            edge = None
            for t in a.targets:
                if t.uv == edgeuv:
                    edge = t
            if (a.weight < b.weight) or (a.weight == b.weight and a.id < b.id):
                if edge.weight == -1:
                    edge.weight = 0
                for t in a.targets:
                    if t.weight == -1:
                        t.weight = 0
                weight_sum = sum([t.weight for t in a.targets])
                remainder = a.weight - edge.weight
                edge.weight = edge.weight + remainder
                a.weight = a.weight - remainder
                b.weight = b.weight - remainder
                a.on = True
                print "turned on node " , a.id
