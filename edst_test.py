import sys
#sys.path.append('/Users/paul/dev/schoolRelated/graphcomplexity/edge/lib')
import unittest
#import node
import node
import targ
import netw
import cove as cov
import auto as aut
import edst as eds
from obal import G as G

class NodeTestCase(unittest.TestCase):
    def setUp(self):
        self.node_0 = node.Node()
        self.node_1 = node.Node()
        self.node_2 = node.Node()
        self.node_3 = node.Node()
        self.node_4 = node.Node()
        self.node_5 = node.Node()
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
        self.nodesource = netw.NodeSource()
        self.nodesource.nodes.append(self.node_0)
        self.nodesource.nodes.append(self.node_1)
        self.nodesource.nodes.append(self.node_2)
        self.nodesource.nodes.append(self.node_3)
        self.nodesource.nodes.append(self.node_4)
        self.nodesource.nodes.append(self.node_5)
        eds.set_neighborhood(self.nodesource)
        eds.set_targets(self.nodesource)

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
        assert len(self.nodesource.targets) == 10
        for i in [a.uv for a in self.nodesource.targets]:
            assert i in [set([0,1]), set([0,4]), set([0,2]), set([1,2]), set([1,4]), set([1,5]), set([2,3]), set([2,4]), set([2,5]), set([4,5])]
        assert set( [a.id for a in self.node_2.neighbors]) == set([3,5,1,0,4])
        assert set([a.id for a in self.node_5.neighbors]) == set([2,4,1])
        for i in [a.uv for a in self.node_3.targets]:
            assert i in [set([2,3])]
        for i in [a.uv for a in self.node_0.targets]:
            assert i in [set([0,2]), set([0,4]), set([0,1])]
        assert len(self.node_0.targets) == 3
                     

suite = unittest.makeSuite(NodeTestCase, 'test')

runner = unittest.TextTestRunner()
runner.run(suite)
