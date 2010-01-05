import sys, getopt
import random as ran
import netw
import nect
from obal import G as G

def main():
    try:
        opts, atgs = getopt.getopt(sys.argv[1:], "fi:r:s:a:u:", ["iterations=", "runs=", "size=", "area=", "unweighted="])
    except getopt.GetoptError:
        sys.exit(2)
    unweighted = False
    i=4
    s=20
    r=20
    d=2
    for o,a in opts:
        if o in ('-i', '--iterations'):
            i=int(a)
        if o in ('-r','--runs'):
            r =int(a)
        if o in ('-s','--size'):
            s=int(a)
        if o in ('-a','--area'):
            G.bounds = int(a)
        if o in ('-u','--unweighted'):
            unweighted = True
            G.low = 15
            G.high = 15
            d = int(a)
    if unweighted:
        noweight_deg = open('unweighted-deg.dat', 'w')
    else: 
        weighted_deg = open('weighted_deg.dat', 'w')
    clik = .5 * (s * (s-1))
    step = int((((clik-d) / (i-1)) + 1))
    for a in range(i):
        fsize, ssize, degre = 0, 0 , 0 
        fwate, swate = 0,0
        count = 0
        if unweighted:
            for j in range(r):
                net = netw.NodeSource()
                net.generate(s, d+a+((a**2/i) * step))
                ssizt = net.seq()
                fsizt = net.once()
                fsize += fsizt
                ssize += ssizt
                degrt = len(net.targets)
                degre += degrt                
                count += 1
            fsiza = fsize/float(count)
            ssiza = ssize/float(count)
            degra = degre / float(count)
            nsize = len(net.nodes)
            print ssiza, " ", fsiza 
            noweight_deg.write("%d %d %d %d\n" %(degra, ssiza, fsiza, a))
        else:
            for j in range(r):
                net = netw.NodeSource()
                net.generate(s, d+a+((a**2/i) * step))
                ssizt, swatt = net.weighted_seq()
                fsizt, fwatt = net.weighted_dist()
                degrt = len(net.targets)
                ssize += ssizt
                swate += swatt
                fsize += fsizt
                fwate += fwatt
                degre += degrt
                count += 1
            fsiza = fsize/float(count)
            ssiza = ssize/float(count)
            fwata = fwate/float(count)
            swata = swate/float(count)
            degra = degre/float(count)
            nsize = len(net.nodes)
            weighted_deg.write("%d %d %d %d %d %d\n" %(degra, ssiza, fsiza, swata, fwata, a))
def mod_dif(f,s):
    diff = map(lambda x,y: x-y, f,s)
    diff_dict = {}
    for a in diff:
        if a not in diff_dict.keys():
            diff_dict[a] = 1
        else:
            diff_dict[a] = diff_dict[a] + 1
    m = max(diff_dict.values())
    for a in diff_dict:
        if diff_dict[a] == m:
            return a

def max_dif(f,s):
    diff = map(lambda x, y: x-y, f, s)
    return max(diff)

main()
