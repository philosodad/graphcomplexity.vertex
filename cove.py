class Cover(object):
    def __init__(self, n):
        self.node_list = n
        self.lifetime = ()
        self.neighbors = []
        self.degree = len(self.neighbors)

    
