import sys
#sys.path.append('/Users/paul/dev/schoolRelated/graphcomplexity/edge/lib')
import unittest
#import node
import node
import targ
import netw
import cove as cov
import auto as aut
from obal import G as G

class NodeTestCase(unittest.TestCase):
    def setUp(self):
        self.node_0 = node.Node()
        self.node_1 = node.Node()
        self.node_2 = node.Node()
        self.node_3 = node.Node()
        self.node_4 = node.Node()
        self.node_5 = node.Node()
        self.target_0 = targ.Target()
        self.target_1 = targ.Target()
        self.target_2 = targ.Target()
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
        self.target_0.x = 300
        self.target_0.y = 300
        self.target_1.x = 200
        self.target_1.y = 200
        self.target_2.x = 250
        self.target_2.y = 325
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
        self.nodesource.targets.append(self.target_0)
        self.nodesource.targets.append(self.target_1)
        self.nodesource.targets.append(self.target_2)
        self.nodesource.set_targets()
        self.nodesource.set_neighborhood()

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
        node.Node.Next_id = 0
        targ.Target.Next_id = 0
        
    def test_ID(self):
        print ("self node 1 has id %s" %(self.node_1.id))
        print ("self node 0 has id %s" %(self.node_0.id))
        assert self.node_1.id == 1

    def test_Loc(self):
        assert self.node_1.x <= G.bound
        assert self.node_1.x >= 0
        print ("Location is %d,%d" %(self.node_0.x, self.node_0.y))
 
    def test_Covers(self):
        self.node_0.build_covers()
        self.node_1.build_covers()
        self.node_3.build_covers()
        self.node_5.build_covers()
        self.node_4.build_covers()
        self.node_2.build_covers()
        print [("%s: %s" %(a.node_list, a.degree)) for a in self.node_4.covers]
        
        for x in set([4]), set ([0,5]), set([5,4]):
            assert x in [a.node_list for a in self.node_4.covers]
        assert not set([5]) in [a.node_list for a in self.node_4.covers]
        assert type(self.node_4.get_cover(set([0,5]))) == cov.Cover
        assert self.node_4.get_cover(set([0,5])).lifetime == 110
        print self.node_4.get_cover(set([0,5])).degree
        assert self.node_4.get_cover(set([0,5])).degree == 5
        assert self.node_4.get_cover(set([2,4])).degree == 8
        assert len(self.node_4.covers) == 11
        assert self.node_2.get_cover(set([2,1])).degree == 19
        x = self.node_4.get_cover(set([0,1]))
        y = self.node_4.get_cover(set([0,5]))
        assert x.degree == y.degree
        assert x < y
        x = self.node_4.get_cover(set([4,5]))
        y = self.node_4.get_cover(set([2,1]))
        assert x.degree == y.degree
        print x.on, y.on
        assert x > y
        print [a for a in self.node_0.covers]
        assert self.node_0.on
        print [a for a in self.node_4.covers]
        aut.automata(self.node_4, self.node_2.id)
        assert not self.node_4.on
        print [a for a in self.node_4.covers]
        print [a for a in self.node_0.covers]

suite = unittest.makeSuite(NodeTestCase, 'test')

runner = unittest.TextTestRunner()
runner.run(suite)

