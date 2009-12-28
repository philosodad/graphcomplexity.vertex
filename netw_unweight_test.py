import sys
#sys.path.append('/Users/paul/dev/schoolRelated/graphcomplexity/edge/lib')
import unittest
#import node
import node
import ctno
import targ
import netw
import nect
import dens
import caut as cau
import neco as cov
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
        self.node_0.battery_life = 110
        self.node_1.battery_life = 110
        self.node_2.battery_life = 110
        self.node_3.battery_life = 110
        self.node_4.battery_life = 110
        self.node_5.battery_life = 110
        self.nodesource.nodes.append(self.node_0)
        self.nodesource.nodes.append(self.node_1)
        self.nodesource.nodes.append(self.node_2)
        self.nodesource.nodes.append(self.node_3)
        self.nodesource.nodes.append(self.node_4)
        self.nodesource.nodes.append(self.node_5)
 
    def tearDown(self):
        self.node_0 = None
        self.node_1 = None
        self.node_2 = None
        self.node_3 = None
        self.node_4 = None
        self.node_5 = None
        self.nodesource = None
        node.Node.Next_id = 0
        targ.Target.Next_id = 0
        ctno.T_Node.Next_id = 0

    def test_once(self):
        dens.set_neighborhood(self.nodesource, 5)
        dens.set_targets(self.nodesource)
        for a in self.nodesource.nodes:
            a.build_covers()
        self.nodesource.once()
        assert self.nodesource.targets_covered()
        print len(filter(lambda a: a.on == True, self.nodesource.nodes))
        print [a.uv for a in self.nodesource.targets]
        

suite = unittest.makeSuite(NetwTestCase, 'test')
runner = unittest.TextTestRunner()
runner.run(suite)
