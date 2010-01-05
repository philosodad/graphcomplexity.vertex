import copy as cop

def gmm(net):

    def saturation(target):
        for a in target.uv:
            if net.keyed_nodes[a].on:
                return True
        return False

    def saturate(a):
        uv = cop.copy(a.uv)
        u = net.keyed_nodes[uv.pop()]
        v = net.keyed_nodes[uv.pop()]
        if u.battery_life < v.battery_life:
            update_weight(a,u)
        else:
            update_weight(a,v)

    def update_weight(t,n):
        w = 0
        for e in n.targets:
            w = w+e.weight
        w = n.battery_life - w
        t.weight = w
        n.on = True

    for a in net.nodes:
        a.on = False
    for a in net.targets:
        if saturation(a):
            a.weight = 0
        else:
            saturate(a)
    on_list = filter(lambda a: a.on == True, net.nodes)
    weight = sum([a.battery_life for a in on_list])
    return len(on_list), weight

