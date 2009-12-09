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
        self.nodesource.network['nodes'][self.node_1.id] = self.node_1
        self.nodesource.network['nodes'][self.node_2.id] = self.node_2   
        self.nodesource.network['nodes'][self.node_3.id] = self.node_3
        self.nodesource.network['nodes'][self.node_4.id] = self.node_4
        self.nodesource.network['nodes'][self.node_5.id] = self.node_5
        self.nodesource.network['nodes'][self.node_6.id] = self.node_6
        self.nodesource.network['targets'][self.target_1.id] = self.target_1
        self.nodesource.network['targets'][self.target_2.id] = self.target_2
        self.nodesource.network['targets'][self.target_3.id] = self.target_3

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

    def testSetTargets(self):
        self.nodesource.set_targets()
        assert self.node_2.targets[self.target_1.id] == self.target_1
        for a in [self.target_3.id]:
            assert a in self.node_1.targets.keys()
        for a in [self.node_4.targets, self.node_3.targets]:
            assert self.target_2.id in a.keys()
        for a in [self.node_2, self.node_5, self.node_6, self.node_1]:
            assert self.target_2.id not in a.targets.keys()
        assert self.target_3.id not in self.node_3.targets.keys()

    def testSetNeighborhood(self):
        self.nodesource.set_neighborhood()
        assert self.node_1.id not in self.node_1.neighbors.keys()
        for a in [self.node_5.id, self.node_3.id, self.node_2.id]:
            assert a in self.node_1.neighbors.keys()
        for a in [self.node_2.id, self.node_6.id, self.node_5.id, self.node_4.id]:
            assert a in self.node_3.neighbors.keys()
          
            
suite = unittest.makeSuite(NodeSourceTestCase, 'test')
runner = unittest.TextTestRunner()
runner.run(suite)
