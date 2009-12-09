import sys
#sys.path.append('/Users/paul/dev/schoolRelated/graphcomplexity/edge/lib')
import unittest
#import node
import node
import targ
import netw
from obal import G as G

class NodeTestCase(unittest.TestCase):
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
        self.nodesource.nodes.append(self.node_1)
        self.nodesource.nodes.append(self.node_2)
        self.nodesource.nodes.append(self.node_3)
        self.nodesource.nodes.append(self.node_4)
        self.nodesource.nodes.append(self.node_5)
        self.nodesource.nodes.append(self.node_6)
        self.nodesource.targets.append(self.target_1)
        self.nodesource.targets.append(self.target_2)
        self.nodesource.targets.append(self.target_3)
        self.nodesource.set_targets()
        self.nodesource.set_neighborhood()

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
        node.Node.Next_id = 0
        targ.Target.Next_id = 0

    def test_ID(self):
        print ("self node 2 has id %s" %(self.node_2.id))
        print ("self node 1 has id %s" %(self.node_1.id))
        assert self.node_2.id == 1

    def test_Loc(self):
        assert self.node_2.x <= G.bound
        assert self.node_2.x >= 0
        print ("Location is %d,%d" %(self.node_1.x, self.node_1.y))
 
    def test_Covers(self):
        self.node_5.build_covers()
        assert set([4]) and set ([0,5]) and set([5,4]) and not set ([5]) in self.node_5.covers
        
suite = unittest.makeSuite(NodeTestCase, 'test')

runner = unittest.TextTestRunner()
runner.run(suite)

