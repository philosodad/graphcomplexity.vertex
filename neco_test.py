import unittest
import neco as cove

class CoveTestCase(unittest.TestCase):
    def setUp(self):
        self.cover_0 = cove.Cover(set([3,4]))
        self.cover_1 = cove.Cover(set([4,5]))
        self.cover_2 = cove.Cover(set([1,2]))
        self.cover_3 = cove.Cover(set([3,5]))
        self.cover_4 = cove.Cover(set([5]))
        self.cover_5 = cove.Cover(set([6,8,9]))
        self.cover_6 = cove.Cover(set([6,7,9]))
        self.cover_0.degree = 2
        self.cover_1.degree = 3
        self.cover_2.degree = 0
        self.cover_3.degree = 3
        self.cover_4.degree = 2
        self.cover_5.degree = 2
        self.cover_6.degree = 2
        self.cover_0.lifetime = 200
        self.cover_4.lifetime = 100
        self.cover_5.lifetime = 150
        self.cover_6.lifetime = 150
        
        self.cover_0.on = 1
        self.cover_1.on = 1
        self.cover_2.on = 2
        self.cover_3.on = 2
        self.cover_4.on = 1
        self.cover_5.on = 2
        self.cover_6.on = 2
        
    def tearDown(self):
        self.cover_0 = None
        self.cover_1 = None
        self.cover_2 = None
        self.cover_3 = None
        self.cover_4 = None

    def test_Cove(self):
        assert self.cover_0 < self.cover_1
        assert self.cover_4 < self.cover_3
        assert self.cover_0 > self.cover_2
        assert self.cover_1 < self.cover_3
        assert self.cover_4 < self.cover_0
        assert self.cover_5 > self.cover_6
        assert self.cover_0 == self.cover_0
        assert self.cover_0 != self.cover_3

suite = unittest.makeSuite(CoveTestCase, 'test')

runner = unittest.TextTestRunner()
runner.run(suite)
