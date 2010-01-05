import copy as cop

def gmm(net):

    def saturation(target):
        for a in target.uv:
            if net.keyed_nodes[a].on:
                return True
        return False

    def saturate(t):
        uv = cop.copy(t.uv)
        u = net.keyed_nodes[uv.pop()]
        v = net.keyed_nodes[uv.pop()]
        if u.weight < v.weight:
            update_weight(t,u)
        else:
            update_weight(t,v)
        u.weight = u.weight - t.weight
        v.weight = v.weight - t.weight

    def update_weight(t,n):
        w = 0
        for e in n.targets:                
            w = w+e.weight
        w = n.weight - w
        t.weight = w
        n.on = True

    for a in net.nodes:
        a.on = False
        a.weight = a.battery_life
    for a in net.targets:
        if saturation(a):
            a.weight = 0
        else:
            saturate(a)
    on_list = filter(lambda a: a.on == True, net.nodes)
    weight = sum([a.battery_life for a in on_list])
    return len(on_list), weight

