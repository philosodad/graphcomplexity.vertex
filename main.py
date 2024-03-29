import sys, getopt
import random as ran
import netw
import nect
from obal import G as G

def main():
    try:
        opts, atgs = getopt.getopt(sys.argv[1:], "fi:r:b:a:d:", ["iterations=", "runs=", "base=", "area=", "density="])
    except getopt.GetoptError:
        sys.exit(2)
    framework_only = False
    density_variation = None
    i=4
    b=5
    r=20
    d=2
    for o,a in opts:
        if o in ('-f'):
            framework_only = True
        if o in ('-i', '--iterations'):
            i=int(a)
        if o in ('-r','--runs'):
            r =int(a)
        if o in ('-b','--base'):
            b=int(a)
        if o in ('-a','--area'):
            G.bounds = int(a)
        if o in ('-d','--density'):
            density_variation = True
            d = int(a)
    cresult_out = open("c_data.dat", 'w')
    fresult_out = open("f_data.dat", 'w')
    sresult_out = open('s_data.dat', 'w')
    for a in range(i):
        fsize, flife, csize, clife, ssize, degre = 0,0,0,0,0,0
        fsizes, ssizes = [], []
        count = 0
        for j in range(r):
            net = netw.NodeSource()
            ne2 = nect.T_NodeSource()
            if not density_variation:
                net.generate(b+b*a, density_variation)
            else:
                print "i = ", i
                print "b = ", b
                net.generate(b*i, int(d*b*i*.5) + (int(b*a*.5))*((b*a)-1))
            ssizt = net.approx
            net.feed_nect(ne2)
            fsizt, flift = net.go()
            if not framework_only:
                csizt, clift = ne2.go()
            else:
                csizt, clift = 5, 5
                fsizes.append(fsizt)
                ssizes.append(ssizt)
                degrt = net.get_degree()
            if csizt != 0:
                fsize += fsizt
                flife += flift
                csize += csizt
                clife += clift
                ssize += ssizt
                count += 1
                degre += degrt
        fsiza = fsize / float(count)
        flifa = flife / float(count)
        csiza = csize / float(count)
        clifa = clife / float(count)
        ssiza = ssize / float(count)
        degra = degre / float(count)
        nsize = len(net.nodes)
        if framework_only:
            fsmod = mod_dif(fsizes, ssizes)
            fsmax = max_dif(fsizes, ssizes)
        fresult_out.write(("%d\t%d\t%d\t%d\n" %(nsize, degra, fsiza, flifa)))
        cresult_out.write(("%d\t%d\t%d\t%d\n" %(nsize, degra, csiza, clifa)))
        if framework_only:
            sresult_out.write(("%d\t%d\t%d\t%d\t%d\n" %(nsize, degra, ssiza, fsmod, fsmax)))

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
