import random as ran
import netw
import nect
import obal

def main():
    net = netw.NodeSource()
    ne2 = nect.T_NodeSource()
    net.generate(10, 5)
    net.feed_nect(ne2)
    net.go()
    ne2.go()
main()
