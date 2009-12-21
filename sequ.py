def sequential(net):
    cover_list = set([])
    for a in net.targets:
        if len(a.uv - cover_list) == 2:
            cover_list = cover_list.union(a.uv)
    return len(cover_list)
            
