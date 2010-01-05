import random as ran
import copy as cop

def init(net):
    for a in net.targets:
        a.weight = -1
    for a in net.nodes:
        a.on = False
        for b in a.neighbors:
            a.keyed_neighbors[b.id] = b

def set_partners(net):
    t_list = []
    for a in net.targets:
        if a.weight == -1:
            t_list.append(a)
    if not t_list:
        return True #the graph is matched
    while t_list:
        edge = ran.choice(t_list)
        print "pulled edge:", edge.uv
        def notmatch(e):
            return len(e.uv - edge.uv) == 2
        t_list = filter(notmatch, t_list)
        g = cop.copy(edge.uv)
        u = g.pop()
        v = g.pop()
        net.keyed_nodes[u].round_partner = v
        net.keyed_nodes[v].round_partner = u

def set_edge(net):
    for a in net.nodes:
        if a.round_partner:
            b = net.keyed_nodes[a.round_partner]
            edgeuv = set([a.id, b.id])
            edge = None
            while edge == None:
                if t.uv == edgeuv:
                    edge = t
            if (a.battery_life < b.battery_life) or (a.battery_life == b.battery_life and a.id < b.id):
                if edge.weight == -1:
                    edge.weight = 0
                for t in a.targets:
                    if t.weight == -1:
                        t.weight = 0
                weight_sum = sum([t.weight for t in a.targets])
                remainder = a.battery_life - edge.weight
                edge.weight = edge.weight + remainder
                a.battery_life = a.battery_life - remainder
                b.battery_life = b.battery_life - remainder
                a.on = True
