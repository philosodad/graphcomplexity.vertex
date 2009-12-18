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

class NodeTestCase(unittest.TestCase):
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
  #      self.nodesourc2 = nect.T_NodeSource()
   #     self.nodesourc3 = netw.NodeSource()
    #    self.nodesource.feed_nect(self.nodesourc2)

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
        ctno.T_Node.Next_id = 0

        
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
        
        for x in [set([4]), set ([1,2,5])]:
            assert x in [a.node_list for a in self.node_4.covers]
        assert not set([5]) in [a.node_list for a in self.node_4.covers]
        assert type(self.node_4.get_cover(set([4]))) == cov.Cover
        assert self.node_4.get_cover(set([1,2,5])).lifetime == 110
        print self.node_4.get_cover(set([1,2,5])).degree
        assert self.node_4.get_cover(set([1,2,5])).degree == 0
        assert self.node_4.get_cover(set([4])).degree == 0
        assert len(self.node_4.covers) == 2
        assert self.node_2.get_cover(set([2])).degree == 0
        x = self.node_4.get_cover(set([4]))
        y = self.node_4.get_cover(set([1,2,5]))
        assert x.degree == y.degree
        assert x.degree == y.degree
        print x.on, y.on
        assert x <> y
        print [a for a in self.node_0.covers]
        assert self.node_0.on
        print [a for a in self.node_4.covers]
        aut.automata(self.node_4, self.node_2.id)
        assert self.node_2.on
        print [a for a in self.node_4.covers]
        print [a for a in self.node_0.covers]
        self.node_4.battery_life = 0
        self.node_2.update_covers()
        assert set([4,0,3]) not in [a.node_list for a in self.node_2.covers]
        assert set([2]) in [a.node_list for a in self.node_2.covers]
        self.node_4.update_covers()
        assert set([4]) not in [a.node_list for a in self.node_4.covers]

suite = unittest.makeSuite(NodeTestCase, 'test')

runner = unittest.TextTestRunner()
runner.run(suite)

