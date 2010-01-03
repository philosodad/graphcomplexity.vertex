#auto.py
#j.paul daigle
#The basic automata for the framework as a whole.

def automata(n):
    def all_on(ids):
        if ids: 
            for a in ids:
                if keyed_nodes[a].on == False:
                    return False
        return True

    def update_on(snl):
        if n.id in snl:
            n.on = True
        else:
            n.on = False

    if not n.current_cover:
        return None
    if len(n.covers) == 0:
        return None
    keyed_nodes = {}
    keyed_nodes[n.id] = n
    for a in n.neighbors:
        keyed_nodes[a.id] = a
        
    if not n.targets_covered():
        scc = n.current_cover
        if n.id in scc.node_list:
            n.on = True
        else:
            n.on = False
        if all_on(scc.node_list):
            for a in n.targets:
                a.covered = True
            for a in n.neighbors:
                automata(a)
        else:
            n.current_cover_index = (n.current_cover_index+1)%len(n.covers)
            n.current_cover = n.covers[n.current_cover_index]
            scc = n.current_cover
            update_on(scc.node_list)
            for a in n.targets:
                a.covered = False
            for a in n.neighbors:
                automata(a)
