import SimPy.Simulation as sim
import random as ran
import scipy as sci
import netw
import nect
import obal

def main():
    sim.initialize()
    net = netw.NodeSource()
    ne2 = nect.T_NodeSource()
    net.generate(10, 5)
    net.feed_nect(ne2)
    sim.simulate(until=400)

main()
