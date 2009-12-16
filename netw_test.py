import sys
import unittest
import netw
import node
import targ
import tast
import edst
import geom as geo
from obal import G as G

class NodeSourceTestCase(unittest.TestCase):
    def setUp(self):
        self.node_1 = node.Node()
        self.node_2 = node.Node()
        self.node_3 = node.Node()
        self.node_4 = node.Node()
        self.node_5 = node.Node()
        self.node_6 = node.Node()
        self.target_1 = targ.Target()
        self.target_2 = targ.Target()
        self.target_3 = targ.Target()
        self.node_1.x = 200
        self.node_1.y = 400
        self.node_2.x = 350
        self.node_2.y = 350
        self.node_3.x = 250
        self.node_3.y = 250
        self.node_4.x = 150
        self.node_4.y = 150
        self.node_5.x = 325
        self.node_5.y = 375
        self.node_6.x = 350
        self.node_6.y = 250
        self.target_1.x = 300
        self.target_1.y = 300
        self.target_2.x = 200
        self.target_2.y = 200
        self.target_3.x = 250
        self.target_3.y = 350
        self.node_1.battery_life = 100
        self.node_2.battery_life = 110
        self.node_3.battery_life = 120
        self.node_4.battery_life = 130
        self.node_5.battery_life = 140
        self.node_6.battery_life = 150
        self.nodesource = netw.NodeSource()
        self.nodesourc2 = netw.NodeSource()
        self.nodesource.nodes.append(self.node_1)
        self.nodesource.nodes.append(self.node_2)
        self.nodesource.nodes.append(self.node_3)
        self.nodesource.nodes.append(self.node_4)
        self.nodesource.nodes.append(self.node_5)
        self.nodesource.nodes.append(self.node_6)
        self.nodesource.targets.append(self.target_1)
        self.nodesource.targets.append(self.target_2)
        self.nodesource.targets.append(self.target_3)

    def tearDown(self):
        self.node_1 = None
        self.node_2 = None
        self.node_3 = None
        self.node_4 = None
        self.node_5 = None
        self.node_6 = None
        self.target_1 = None
        self.target_2 = None
        self.target_3 = None
        self.nodesource = None
        self.nodesourc2 = None
        node.Node.Next_id = 0
        targ.Target.Next_id = 0

    def testSetTargets(self):
        tast.set_targets(self.nodesource)
        for a in [self.node_4, self.node_3]:
            assert self.target_2 in a.targets
        for a in [self.node_1, self.node_5]:
            assert self.target_3 in a.targets

    def testSetNeighborhood(self):
        tast.set_neighborhood(self.nodesource)
        assert self.node_1 not in self.node_1.neighbors
        for a in [self.node_5, self.node_3, self.node_2]:
            assert a in self.node_1.neighbors
        for a in [self.node_1, self.node_2, self.node_4, self.node_5, self.node_6]:
            assert a in self.node_3.neighbors

    def testFeed(self):
        self.nodesource.targets = []
        edst.set_neighborhood(self.nodesource)
        edst.set_targets(self.nodesource)
        self.nodesource.feed(self.nodesourc2)
        print [("%s" %(a.uv)) for a in self.nodesource.targets]
        print [("%s" %(b.uv)) for b in self.nodesourc2.targets]
        assert self.nodesource.id != self.nodesourc2.id
        assert len(self.nodesource.targets) > 0
        assert len(self.nodesource.targets) == len(self.nodesourc2.targets)
        for i in range(len(self.nodesource.targets)):
            assert self.nodesource.targets[i] != self.nodesourc2.targets[i]
        assert len(self.nodesource.nodes) > 0
        assert len(self.nodesource.nodes) == len(self.nodesourc2.nodes)
        for i in range(len(self.nodesource.nodes)):
            assert self.nodesource.nodes[i].x == self.nodesourc2.nodes[i].x
            assert self.nodesource.nodes[i].id != self.nodesourc2.nodes[i].id
            assert len(self.nodesource.nodes[i].targets) == len(self.nodesourc2.nodes[i].targets)
suite = unittest.makeSuite(NodeSourceTestCase, 'test')
runner = unittest.TextTestRunner()
runner.run(suite)
