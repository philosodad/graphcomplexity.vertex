import sys
#sys.path.append('/Users/paul/dev/schoolRelated/graphcomplexity/edge/lib')
import unittest
#import node
import node
from obal import G as G

class NodeTestCase(unittest.TestCase):
    def setUp(self):
        self.node_1 = node.Node()
        self.node_2 = node.Node()
    def tearDown(self):
        self.node_1 = None
        self.node_2 = None
    def testID(self):
        assert self.node_2.id == 1
    def testLoc(self):
        assert self.node_2.x <= G.bound
        assert self.node_2.x >= 0
        print ("Location is %d,%d" %(self.node_1.x, self.node_1.y))

suite = unittest.makeSuite(NodeTestCase, 'test')

runner = unittest.TextTestRunner()
runner.run(suite)

