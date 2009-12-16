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
        self.netw_2 = nect.T_NodeSource()
        self.netw_1.feed_nect(self.netw_2)
        print [a.uv for a in self.netw_2.targets]

    def tearDown(self):
        self.netw_1 = None
        self.netw_2 = None

    def test_targets(self):
        assert self.netw_1 != self.netw_2

suite = unittest.makeSuite(NectTestCase, 'test')
runner = unittest.TextTestRunner()
runner.run(suite)
