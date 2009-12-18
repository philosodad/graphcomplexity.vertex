import sys
#sys.path.append('/Users/paul/dev/schoolRelated/graphcomplexity/edge/lib')
import unittest
#import node
import node
import ctno
import targ
import netw
import nect
import edst
import caut as cau
import cove as cov
import auto as aut
from obal import G as G

class NetwTestCase(unittest.TestCase):
    def setUp(self):
        self.nodesource = netw.NodeSource()
        self.node_0 = node.Node(self.nodesource)
        self.node_1 = node.Node(self.nodesource)
        self.node_2 = node.Node(self.nodesource)
        self.node_3 = node.Node(self.nodesource)
        self.node_4 = node.Node(self.nodesource)
        self.node_5 = node.Node(self.nodesource)
        self.node_0.x, self.node_0.y = 200, 375
        self.node_1.x, self.node_1.y = 375, 375
        self.node_2.x, self.node_2.y = 250, 250
        self.node_3.x, self.node_3.y = 150, 150
        self.node_4.x, self.node_4.y = 375, 300
        self.node_5.x, self.node_5.y = 375, 150
        self.node_0.battery_life = 100
        self.node_1.battery_life = 110
        self.node_2.battery_life = 80
        self.node_3.battery_life = 130
        self.node_4.battery_life = 120
        self.node_5.battery_life = 110
        self.nodesource.nodes.append(self.node_0)
        self.nodesource.nodes.append(self.node_1)
        self.nodesource.nodes.append(self.node_2)
        self.nodesource.nodes.append(self.node_3)
        self.nodesource.nodes.append(self.node_4)
        self.nodesource.nodes.append(self.node_5)
        edst.set_neighborhood(self.nodesource)
        edst.set_targets(self.nodesource)
        self.nodesourc2 = nect.T_NodeSource()
       # self.nodesource.feed_nect(self.nodesourc2)

    def tearDown(self):
        self.node_0 = None
        self.node_1 = None
        self.node_2 = None
        self.node_3 = None
        self.node_4 = None
        self.node_5 = None
        self.nodesource = None
        for n in self.nodesourc2.nodes:
            n = None
        for n in self.nodesourc2.targets:
            n = None
        self.nodesourc2 = None
        node.Node.Next_id = 0
        targ.Target.Next_id = 0
        ctno.T_Node.Next_id = 0

    def testSetNeighborhood(self):
        assert self.node_1 not in self.node_1.neighbors
        for a in [self.node_5, self.node_3, self.node_2, self.node_1]:
            assert a not in self.node_1.neighbors
        for a in [self.node_2, self.node_1, self.node_5]:
            assert a in self.node_4.neighbors

    def test_targetsCovered(self):
        assert self.nodesource.targets_covered()
        assert self.node_2.on
        self.node_2.on = False
        self.node_3.on = False
        assert not self.nodesource.targets_covered()

    def test_go(self):
        for a in self.nodesource.nodes:
            a.build_covers()
        self.nodesource.go()

suite = unittest.makeSuite(NetwTestCase, 'test')
runner = unittest.TextTestRunner()
runner.run(suite)
