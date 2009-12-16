import SimPy.Simulation as sim
import random as ran
import scipy as sci
import node as nod
import targ as tar
import geom as geo
import auto as aut
import tast as tas
import edst as eds
from obal import G as G

class NodesTwo(sim.Process):
    nodes = []
    targets = []
    Next_id = 0
    def __init__(self):
        sim.Process.__init__(self, name="nodestwo"+str(NodesTwo.Next_id))
        self.id = NodesTwo.Next_id
        NodesTwo.Next_id += 1
