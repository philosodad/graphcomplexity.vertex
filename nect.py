import SimPy.Simulation as sim
import random as ran
import node as nod
import targ as tar
import geom as geo
import auto as aut
import tast as tas
import edst as eds
from obal import G as G


class T_NodeSource(sim.Process):
    nodes = []
    targets = []
    Next_id = 0
    def __init__(self):
        sim.Process.__init__(self, name="nodestwo"+str(T_NodeSource.Next_id))
        self.id = T_NodeSource.Next_id
        T_NodeSource.Next_id += 1
        self.t_source_out = open("t_source.dat", 'w')
        

    def output(self, time):
        x = len(self.targets)
        y = len(filter(lambda a: a.covered, self.targets))
        self.t_source_out.writelines("%d: %d targets, %d covered\n" %(time,x,y))
