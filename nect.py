import SimPy.Simulation as sim
import random as ran
import netw
import caut as cau
from obal import G as G


class T_NodeSource(netw.NodeSource):
    Next_id = 0
    def __init__(self):
        self.id = T_NodeSource.Next_id
        T_NodeSource.Next_id += 1
        self.nodes = []
        self.targets = []
        

    def once(self):
        if self.targets:
            if self.targets_coverable():
                self.set_targets()

    def output(self, time):
        x = len(self.targets)
        y = len(filter(lambda a: a.covered, self.targets))
        self.t_source_out.writelines("%d: %d targets, %d covered\n" %(time,x,y))

    def targets_covered(self):
        on_list = set([b.id for b in filter(lambda a: a.on, self.nodes)])
        if len(on_list) == 0:
            return False
        for a in self.targets:
            if len(a.uv - on_list) == 2:
                return False
        return True

    def targets_coverable(self):
        live_list = set([b.id for b in filter(lambda a: a.battery_life > 0, self.nodes)])
        if len(live_list) == 0:
            return False
        if len(self.targets) == 0:
            return False
        for a in self.targets:
            if len(a.uv - live_list) == 2:
                return False
        for a in self.targets:
            live_mark = 0
            for b in a.uv:
                if b in live_list:
                    live_mark += 1
            if live_mark == 0:
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
