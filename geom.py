
def dist(ob_1, ob_2):
    a_squared = (ob_1.x - ob_2.x)**2
    b_squared = (ob_1.y - ob_2.y)**2
    c = (a_squared + b_squared)**.5
    return c

def key_targets(n):
    keyed_targets = {}
    for a in n.targets:
        x = (a.uv - set([n.id])).pop()
        keyed_targets[x] = a
    return keyed_targets
