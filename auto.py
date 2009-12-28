#auto.py
#j.paul daigle
#The basic automata for the framework as a whole.

def automata(n, sender):
    while 1:
        n.update_covers()
        if not n.current_cover:
            return None
        if len(n.covers) == 0:
            return None
        if n.covers[n.current_cover_index%len(n.covers)] != n.current_cover:
            n.current_cover_index = (n.current_cover_index + 1)%len(n.covers)
            n.current_cover = n.covers[n.current_cover_index]
            n.current_cover_index = 0

        scc = n.current_cover
        keyed_neighbors = {}
        for a in n.neighbors:
            keyed_neighbors[a.id] = a
        if ((sender in scc.node_list and keyed_neighbors[sender].on is True) or (sender not in scc.node_list and keyed_neighbors[sender] is False)) and ((n.id not in scc.node_list and n.on is False) or (n.id in scc.node_list and n.on is True)):
            return None #keep current cover

        #if s is not in current cover and everything else in the cover is on or everything is off
        elif (n.id not in scc.node_list and (set([keyed_neighbors[a].on for a in scc.node_list]) - set([True]) == set([]))):
            if n.on:
                n.on = False
                print "turned ", n.id, " off. ", n.on
                scc.covered = True
                n.update_covers()
                for a in n.neighbors:
                    print("%s calling %s.auto" %(n.id, a.id))
                    automata(a, n.id)
                return None
            else:
                return None

        #if s IS in the current cover and everything but s in the cover is on or everything is off
        elif (n.id in scc.node_list and (len(set([keyed_neighbors[a].on for a in (scc.node_list-set([n.id]))])) < 2)):
            if not n.on:
                n.on = True
                print "turned ", n.id, " on. ", n.on
                scc.covered = True
                n.update_covers()
                for a in n.neighbors:
                    automata(a, n.id)
                    return None
            else:
                return None
        
        elif(len(set([keyed_neighbors[a].on for a in (scc.node_list - set([n.id]))])) > 1):
            n.current_cover_index = (n.current_cover_index + 1)%(len(n.covers))
            n.current_cover = n.covers[n.current_cover_index]
        else:
            return None
