import random as ran
from obal import G as G

big = G.big_constant

def t_algorithm(n):
    if not n.targets:
        return None
    if len(set([a.covered for a in n.targets])) == 1 and n.targets[0].covered == True:
        return None
    keyed_neighbors = {}
    for a in n.neighbors:
        keyed_neighbors[a.id] = a
    keyed_targets = {}
    for a in n.targets:
        x = (a.uv - set([n.id])).pop()
        keyed_targets[x] = a
    if ran.randint(0,1) == 0:
        n.root = True
        print ("root %d" %(n.id))
    else:
        print "not root ", n.id
        n.root = False
    print n.root
    if not n.root:
        for a in n.neighbors:
            print a.root
            if a.root:
                print a.id, " is a root!"
                if step_check(n, a):
                    print "step check returns true"
                    keyed_targets[a.id].active = True
            x = filter(lambda a: a.active, n.targets)
            if x:
                x = ran.choice(x)
                x.star_edge = True
                print "a random choice has been made ", x.id, x.star_edge
            else:
                print "no active edges for ", n.id
    else:
        print "process ", n.id
        if ran.randint(0,1) == 0:
            if not n.on:
                print n.id, " is off"
                for a in filter(lambda t: t.star_edge, n.targets):
                    print "lets step"
                    step(keyed_neighbors[(a.uv - set([n.id])).pop()], n)
        else:
            if filter(lambda t: t.star_edge, n.targets):
                a = filter(lambda t: t.star_edge, n.targets).pop()
                step(keyed_neighbors[((a.uv) - set([n.id])).pop()], n)
                    

def step_check(v, w):
    print v.ex
    print "before calculation, beta should be ", (1-v.ex) * big-v.battery_life
    beta = min([(1-v.ex)*(big-v.battery_life), (1-w.ex)*(big-w.battery_life)])
    print ("beta %s: %s" %(v.id, beta))
    if v.ex + (beta / float(big-v.battery_life)) == 1:
        return True
    else:
        return False


def step(v,w):
    beta = min([(1-v.ex)*(big-v.battery_life), (1-w.ex)*(big-w.battery_life)])
    print ("step beta %s: %s" %(v.id, beta))
    v.ex = v.ex + (beta/float(big-v.battery_life))
    w.ex = w.ex + (beta/float(big-w.battery_life))
    if v.ex == 1:
        v.on = True
        for a in v.targets:
            a.covered = True
    if w.ex == 1:
        w.on = True
        for a in w.targets:
            a.covered = True
