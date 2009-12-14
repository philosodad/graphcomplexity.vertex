import cove as cov

def build_covers(self):
    bil.init_covers(n)
    bil.update_degree(n)
    bil.update_lifetime(n)
    bil.update_on(n)

def init_covers(n):
    big_list = {}
    big_list = big_list.fromkeys(n.targets)
    for a in big_list:
        big_list[a] = [n.id]
        
    for a in n.neighbors:
        for b in big_list.keys():
            if b in a.targets:
                big_list[b].append(a.id)
        
    small_list = big_list.values()
    slots = 1
    for a in small_list:
        slots = slots * len(a)
    c = []
    for i in range(slots):
        c.append([])
    b = 1
    for i in range(len(small_list)):
        g = 0
        f = 0
        while g < len(c):
            for j in range(b):
                c[g].append(small_list[i][f%len(small_list[i])])
                g+=1
            f+=1
        b = b * len(small_list[i])
            
    for a in c:
        if set(a) not in [b.node_list for b in n.covers]:
            n.covers.append(cov.Cover(set(a)))

def update_degree(n):
    for a in n.covers:
        a.degree = 0
        for b in n.covers:
            if  a != b:
                a.degree += len(a.node_list.intersection(b.node_list))    

def update_lifetime(n):
    keyed_lifetimes = {}
    keyed_lifetimes[n.id] =  n.battery_life
    for a in n.neighbors:
        keyed_lifetimes[a.id] = a.battery_life
    for a in n.covers:
        lives = []
        for b in a.node_list:
            lives.append(keyed_lifetimes[b])
        lives.sort()
        try:
            a.lifetime = lives.pop()
        except:
            print ("node %s failed for %s" %(n.id, a.node_list))

def update_on(n):
    keyed_on = {}
    keyed_on[n.id] = n.on
    for a in n.neighbors:
        keyed_on[a.id] = a.on
    #    print ("%s thinks %s.on is %s" %(n.id, a.id, keyed_on[a.id]))
    for a in n.covers:
        a.on = 0
        for b in a.node_list:
            if keyed_on[b]:
                a.on += 1
        a.on = len(a.node_list) - a.on

