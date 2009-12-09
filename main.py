import SimPy.Simulation as sim
import random as ran
import scipy as sci
import netw
import obal

def main():
    sim.initialize()
    net = netw.NodeSource()
    net.generate(50, 10)
    sim.simulate(until=200)

main()
