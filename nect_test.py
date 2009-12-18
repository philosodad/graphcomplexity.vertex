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

class NectTestCase(unittest.TestCase):
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
        self.nodesourc3 = nect.T_NodeSource()
        self.nodesource.feed_nect(self.nodesourc3)

    def tearDown(self):
        self.node_0 = None
        self.node_1 = None
        self.node_2 = None
        self.node_3 = None
        self.node_4 = None
        self.node_5 = None
        self.target_0 = None
        self.target_1 = None
        self.target_2 = None
        self.nodesource = None
        self.nodesourc2 = None
        self.nodesourc3 = None
        node.Node.Next_id = 0
        targ.Target.Next_id = 0
        ctno.T_Node.Next_id = 0

    def test_targets(self):
        nodesourc2 = nect.T_NodeSource()
        self.nodesource.feed_nect(nodesourc2)
        assert self.nodesource != nodesourc2
        n = nodesourc2.nodes[0]
        p = nodesourc2.nodes[1]
        m = nodesourc2.nodes[2]
        o = nodesourc2.nodes[3]
        assert nodesourc2.targets_coverable()
        m.battery_life = 0
        n.battery_life = 0
        o.battery_life = 0
        p.battery_life = 0
        for a in nodesourc2.nodes:
            print a.battery_life
        assert not nodesourc2.targets_coverable()

    def test_go(self):
        self.nodesourc3.go()
        assert True

suite = unittest.makeSuite(NectTestCase, 'test')
runner = unittest.TextTestRunner()
runner.run(suite)
