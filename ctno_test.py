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

class T_NodeTestCase(unittest.TestCase):
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
        self.nodesource = netw.NodeSource()
        self.nodesource.nodes.append(self.node_0)
        self.nodesource.nodes.append(self.node_1)
        self.nodesource.nodes.append(self.node_2)
        self.nodesource.nodes.append(self.node_3)
        self.nodesource.nodes.append(self.node_4)
        self.nodesource.nodes.append(self.node_5)
        edst.set_neighborhood(self.nodesource)
        edst.set_targets(self.nodesource)
        self.nodesourc2 = nect.T_NodeSource()
        self.nodesource.feed_nect(self.nodesourc2)

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

    def testBasics(self):
        print [a.uv for a in self.nodesource.targets]
        for a in self.nodesource.nodes:
            print [b.uv for b in a.targets]
        assert len(self.nodesource.targets)==5
        assert len(self.nodesourc2.targets)==5
        for a in self.nodesource.nodes:
            a.build_covers
        for a in self.nodesource.nodes:
            for b in a.neighbors:
                aut.automata(b, a.id)
        while self.nodesourc2.targets[0].covered == False:
            for n in self.nodesourc2.nodes:
                print n.id
                cau.t_algorithm(n)
        for n in self.nodesourc2.nodes:
            assert n.x != 0
        print [a.id for a in filter(lambda b: b.on, self.nodesourc2.nodes)]
        print [a.id for a in filter(lambda b: b.on, self.nodesource.nodes)]

suite = unittest.makeSuite(T_NodeTestCase, 'test')

runner = unittest.TextTestRunner()
runner.run(suite)
