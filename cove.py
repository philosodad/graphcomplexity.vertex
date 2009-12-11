class Cover(object):
    def __init__(self, n):
        self.node_list = n
        self.lifetime = ()
        self.degree = 0
        self.on = 0

    def __eq__(self, other):
        return id(self) == id(other)

    def __ne__(self, other):
        return id(self) != id(other)

    def __cmp__(self, other):
        if self.degree < other.degree:
            return -1
        elif self.degree > other.degree:
            return 1
        elif self.on < other.on:
            return 1
        elif self.on > other.on:
            return -1
        else:
            if min(self.node_list) < min(other.node_list):
                return -1
            elif min(other.node_list) < min(self.node_list):
                return 1
            else:
                x = self.node_list.difference(other.node_list)
                y = other.node_list.difference(self.node_list)
                if len(x) == 0:
                    return 1
                elif len(y) == 0:
                    return -1
                elif min(x) < min(y):
                    return -1
                else:
                    return 1
    
