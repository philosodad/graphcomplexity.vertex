import random as ran
import netw
import nect
import obal

def main():
    for i in range(4):
        t_source_out = open(("%d_sourc2.dat" %(i)), 'w')
        source_out = open(("%d_source.dat" %(i)), 'w')
        for j in range(20):
            net = netw.NodeSource(source_out)
            ne2 = nect.T_NodeSource(t_source_out)
            net.generate(5+5*i, 5)
            net.feed_nect(ne2)
            net.go()
            ne2.go()
main()
