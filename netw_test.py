import sys
import unittest
import netw
import node
import targ

class NodeSourceTestCase(unittest.TestCase):
    def setUp(self):
        self.node_1 = node.Node()
        self.node_2 = node.Node()
        self.node_3 = node.Node()
        self.target_1 = targ.Target()
        self.node_1.x = 400
        self.node_1.y = 400
        self.node_2.x = 350
        self.node_2.y = 350
        self.node_3.x = 250
        self.node_3.y = 250
        self.target_1.x = 300
        self.target_1.y = 300
        self.nodesource = netw.NodeSource()
        self.nodesource.network['nodes'][self.node_1.id] = self.node_1
        self.nodesource.network['nodes'][self.node_2.id] = self.node_2   
        self.nodesource.network['nodes'][self.node_3.id] = self.node_3
        self.nodesource.network['targets'][self.target_1.id] = self.target_1
    def tearDown(self):
        self.node_1 = None
        self.node_2 = None
        self.node_3 = None
        self.target_1 = None
        self.nodesource = None
    def testSetTargets(self):
        self.nodesource.set_targets()
        assert self.node_2.targets[self.target_1.id] == self.target_1
        print self.node_1.targets
        assert self.target_1.id not in self.node_1.targets  

suite = unittest.makeSuite(NodeSourceTestCase, 'test')
runner = unittest.TextTestRunner()
runner.run(suite)
