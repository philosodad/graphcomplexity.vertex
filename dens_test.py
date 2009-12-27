import sys
#sys.path.append('/Users/paul/dev/schoolRelated/graphcomplexity/edge/lib')
import unittest
#import node
import node
import targ
import netw
import cove as cov
import auto as aut
import dens as den
from obal import G as G

class NodeTestCase(unittest.TestCase):
    def setUp(self):
        self.nodesource = netw.NodeSource()
        self.node_0 = node.Node(self.nodesource)
        self.node_1 = node.Node(self.nodesource)
        self.node_2 = node.Node(self.nodesource)
        self.node_3 = node.Node(self.nodesource)
        self.node_4 = node.Node(self.nodesource)
        self.node_5 = node.Node(self.nodesource)
        self.node_0.x = 200
        self.node_0.y = 375
        self.node_1.x = 350
        self.node_1.y = 350
        self.node_2.x = 250
        self.node_2.y = 250
        self.node_3.x = 150
        self.node_3.y = 150
        self.node_4.x = 325
        self.node_4.y = 350
        self.node_5.x = 350
        self.node_5.y = 250
        self.node_0.battery_life = 100
        self.node_1.battery_life = 110
        self.node_2.battery_life = 120
        self.node_3.battery_life = 130
        self.node_4.battery_life = 120
        self.node_5.battery_life = 110
        self.nodesource.nodes.append(self.node_0)
        self.nodesource.nodes.append(self.node_1)
        self.nodesource.nodes.append(self.node_2)
        self.nodesource.nodes.append(self.node_3)
        self.nodesource.nodes.append(self.node_4)
        self.nodesource.nodes.append(self.node_5)
        den.set_neighborhood(self.nodesource, 10)
        den.set_targets(self.nodesource)

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
    
    def test_eds_neighborhoods(self): 
        print len(self.nodesource.targets)
        assert len(self.nodesource.targets) == 10
        for a in self.nodesource.nodes:
            print a.neighbors
                     

suite = unittest.makeSuite(NodeTestCase, 'test')

runner = unittest.TextTestRunner()
runner.run(suite)
