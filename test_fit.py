from numpy import *
import sys
#index = int(sys.argv[1])

eV = 13.6057

from scipy.interpolate import lagrange
ds=loadtxt("Cu-bz-PEC-vdw-df.txt")[:,0]
Es=loadtxt("Cu-bz-PEC-vdw-df.txt")[:,1]

Eref=(-21827.1490060017)+(-76.5789527269)
Etot=(Es-Eref)
print ds,Es, Eref, Etot

ind=argmin(Etot)
print ind

def construct_polynomial():
    Etot_min = Etot[ind-1:ind+3]
    ds_min = ds[ind-1:ind+3]
    poly = lagrange(ds_min, Etot_min)
    return poly

poly = construct_polynomial()

d_dense = linspace(ds[ind-2],ds[ind+5],1000)
E_dense = poly(d_dense)
ind_min = argmin(poly(d_dense))

d_min = d_dense[ind_min]
E_min = poly(d_min)

def plot_test():
    from pylab import *
    plot(ds,Etot*eV,'o')
    plot(d_dense,E_dense*eV)
    xlim(min(d_dense),max(d_dense))
    plot(d_min,E_min*eV,marker='x',color='r',markersize=20,markeredgewidth=1)
    ylim(E_min*eV*1.25,E_min*eV*0.05)
    show()

print d_min, E_min*eV 

plot_test()
