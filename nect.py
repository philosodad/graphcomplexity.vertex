import SimPy.Simulation as sim
import random as ran
import node as nod
import targ as tar
import geom as geo
import auto as aut
import tast as tas
import edst as eds
import caut as cau
from obal import G as G


class T_NodeSource(object):
    Next_id = 0
    def __init__(self):
        self.nodes = []
        self.targets = []
        self.id = T_NodeSource.Next_id
        T_NodeSource.Next_id += 1
        self.t_source_out = open("t_source.dat", 'w')
        

    def go(self):
        time = 0
        x = 0
        while self.targets_coverable():
            self.set_targets()
            self.nodes.sort()
            current_node = filter(lambda a: a.on, self.nodes)[0]
            time = time + current_node.battery_life
            print "t_time: ", time, "cover: ", [a.id for a in filter(lambda b: b.on, self.nodes)]
            current_node.on = False
            for a in filter(lambda a: a.on, self.nodes):
                print ("node %s battery life %d" %(a.id, a.battery_life))
                a.battery_life = a.battery_life - current_node.battery_life
                print ("node %s battery life %d" %(a.id, a.battery_life))
#                a.battery_life = 0
            current_node.battery_life = 0
            

    def output(self, time):
        x = len(self.targets)
        y = len(filter(lambda a: a.covered, self.targets))
        self.t_source_out.writelines("%d: %d targets, %d covered\n" %(time,x,y))

    def targets_covered(self):
        on_list = set([b.id for b in filter(lambda a: a.on, self.nodes)])
        for a in self.targets:
            if len(a.uv - on_list) == 2:
                return False
        return True

    def targets_coverable(self):
        live_list = set([b.id for b in filter(lambda a: a.battery_life > 0, self.nodes)])
        for a in self.targets:
            if len(a.uv - live_list) == 2:
                return False
        return True
        
    def set_targets(self):
        for t in self.targets:
            t.active = False
            t.covered = False
            t.star_edge = False
        for n in self.nodes:
            n.ex = 0
            n.on = False
            n.root = False
            n.active = False
        while not self.targets_covered():
            for a in self.nodes:
                cau.t_algorithm(a)
