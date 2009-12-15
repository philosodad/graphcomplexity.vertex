import SimPy.Simulation as sim
import random as ran
import scipy as sci
import netw
import obal

def main():
    sim.initialize()
    net = netw.NodeSource()
    net.generate(5, 5)
    sim.simulate(until=400)

main()
