#bedg.py
#j.paul daigle
#This files constructs all of the cover sets, using the definition of a cover and a target found in targ.py and cove.py

import neco as cov


def init_covers(n):
    n.covers.append(cov.Cover((set([n.id]))))
    id_list = []
    for a in n.neighbors:
        id_list.append(a.id)
    n.covers.append(cov.Cover((set(id_list))))
    for a in n.neighbors:
        a.n_covers.extend(n.covers)
            
def update_lifetime(n):
    keyed_lifetimes = {}
    keyed_lifetimes[n.id] =  n.battery_life
    for a in n.neighbors:
        keyed_lifetimes[a.id] = a.battery_life
    for a in n.covers:
        lives = []
        for b in a.node_list:
            lives.append(keyed_lifetimes[b])
        try:
            a.lifetime = sum(lives)
        except:
            print ("node %s failed for %s" %(n.id, a.node_list))

def update_degree(n):
    keyed_weights = {}
    keyed_weights[n.id] = n.battery_life
    for a in n.neighbors:
        keyed_weights[a.id] = a.battery_life
    for a in n.covers:
        a.degree = 0
        conflicts = []
        for b in n.covers:
            if  a != b:
                if (a.node_list.intersection(b.node_list)) != set([]):
                    conflicts.append(b)
        for b in n.n_covers:
            if  a != b:
                if (a.node_list.intersection(b.node_list)) != set([]):
                    conflicts.append(b)
        for b in conflicts:
            a.degree += b.lifetime


def update_on(n):
    keyed_on = {}
    keyed_on[n.id] = n.on
    for a in n.neighbors:
        keyed_on[a.id] = a.on
        #print ("%s thinks %s.on is %s" %(n.id, a.id, keyed_on[a.id]))
    for a in n.covers:
        a.on = 0
        for b in a.node_list:
            if keyed_on[b]:
                a.on += 1
        a.on = len(a.node_list) - a.on

