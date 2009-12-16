import sys
import copy
#sys.path.append('/Users/paul/dev/schoolRelated/graphcomplexity/edge/lib')
import unittest
import node
import targ
import netw
import nect
import cove as cov
import auto as aut
import edst as eds
from obal import G as G

class NectTestCase(unittest.TestCase):
    def setUp(self):
        self.netw_1 = netw.NodeSource()
        self.netw_1.generate(5,5)
        print [a.uv for a in self.netw_1.targets]
        self.netw_2 = nect.NodesTwo()
        print [a.uv for a in self.netw_2.targets]
        for i in self.netw_1.targets:
            t = copy.copy(i)
            self.netw_2.targets.append(t)
        for i in self.netw_1.nodes:
            t = copy.copy(i)
            self.netw_2.nodes.append(i)


    def tearDown(self):
        self.netw_1 = None
        self.netw_2 = None

    def test_targets(self):
        assert self.netw_1 != self.netw_2
        print [a.uv for a in self.netw_1.targets]
        for i in  [a.uv for a in self.netw_1.targets]:
            assert i in [b.uv for b in self.netw_2.targets]
        for a in self.netw_1.targets:
            assert a not in self.netw_2.targets
        assert len(self.netw_1.targets) == len(self.netw_2.targets)
        assert len(self.netw_1.nodes)== len(self.netw_2.nodes)
#        for i,j in [[a.covers, b.covers] for a in self.netw_1.nodes for b in self.netw_2.nodes]:
 #           assert len(i) == len(j)
        for i,j in [[a.covers, b.covers] for a in self.netw_1.nodes for b in self.netw_2.nodes]:
            print "i: %s" %(i)
            print "j: %s" %(j)

suite = unittest.makeSuite(NectTestCase, 'test')
runner = unittest.TextTestRunner()
runner.run(suite)
