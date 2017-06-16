#!/usr/bin/env python3

from numpy import *
#from pylab import *
from string import *
import sys

# Read in options
# arg 1 is simulation run time, in sec.
# arg 2 is angular resolution parameter
# arg 3 is finest grid spacing, in km
# arg 4 is number of refine levels to compute

tmax = float(sys.argv[1])
radiusFact = float(sys.argv[2])
delXmin = float(sys.argv[3]) # in km
lref = int(sys.argv[4])

#some constants
nblkx = 12.
ndim = 3
avShR = 150 # km

# Flags for various different assumptions
anteS = False
leak = False
M1 = True
energyCoupling = True
prebounce = False
octant = False
subCycle = False
mri = True
turbRes = False
trackShock = False

# MRI/turbulence resolution stuff
mri_levels = 2
dx_turb = 0.488
dx_mri = delXmin / 2.**mri_levels
if mri:
    print('dx_mri', dx_mri)


if prebounce:
    cs = 0.1e5 #km/s, pre-bounce
elif M1:
    cs = 3.0e5 #km/s, M1
#elif anteS:
#    cs = 2e4  #km/s, no PNS
else:
    cs = 1e5 #km/s, post-bounce

#antesonic:
#cs = 2e4

cfl = 0.5
if M1:
    cfl = 0.9
elif mri:
    if ndim==2:
        cfl = 0.4

#cpuHrPerZnStp = 1.89e-7 # pure hydro on Intrepid
#cpuHrPerZnStp = 8.94e-08 # optimized pure hydro on Intrepid WITHOUT Leakage
#cpuHrPerZnStp = 1.88e-7 # optimized pure hydro on Intrepid with 4 threads WITH Leakage
#cpuHrPerZnStp = 2.7e-7 # MHD on Intrepid
#cpuHrPerZnStp = 2.0e-6 # pure UHD on Intrepid with MESA Approx21
#cpuHrPerZnStp = 1.20e-7 # udhopt+leakage on Mira with c8, 4 threads/rank
#cpuHrPerZnStp = 1.07e-7 # udhopt+leakage on Mira with c8, 8 threads/rank
#cpuHrPerZnStp = 0.00048828125/3600 # MHD on vesta
#cpuHrPerZnStp = 1.3e-7 # MHD on vesta/Mira with 24^3 blocks and 6 guardcells, PPM
#cpuHrPerZnStp = 1.0e-7 # MHD on vesta/Mira with 24^3 blocks and 6 guardcells, WENO
#cpuHrPerZnStp = 0.5e-7 # UHD on vesta/Mira with 16^3 blocks and 6 guardcells, WENO
#cpuHrPerZnStp = 6.87e-7  # 3 neutrino radiation groups plus MHD on Mira
#cpuHrPerZnStp = 1.91e-7  # 3 neutrino radiation (reduced resolution) groups plus MHD on Mira
#cpuHrPerZnStp = 1.25e-6**8  # 3 neutrino flavors/16 energy groups (reduced resolution) plus MHD on Mira
#cpuHrPerZnStp = 4.0e-7 # UHD + Aprox19 on Intrepid
#cpuHrPerZnStp = 1.2e-8 # UHD + Leakage on Stampede
#cpuHrPerZnStp = 1.67e-8 # UHD + Aprox21 2D on Stampede
#cpuHrPerZnStp = 1.44e-7 # UHD + Aprox21 3D on Stampede
cpuHrPerZnStp = 2e-7 # UHD + Leakage on Mira
cpuHrPerZnStp = 1.5e-7 # Spark + Aprox21 on Mira

#if leak:
    #cpuHrPerZnStp += 1e-8 # plus Leakage 75x37x1000 rays
if M1:
    if energyCoupling:
        cpuHrPerZnStp = 7.2e-7 # M1 with 3 species, 18 energy groups, energy bin coupling, velocity terms
        cpuHrPerZnStp = 2.5e-6
    else:
        cpuHrPerZnStp += 4.2e-7 # M1 with 3 species, 18 energy groups
        cpuHrPerZnStp = 8.e-7 # 16 threads per rank, 12 energy groups, 24^3
        cpuHrPerZnStp = 3.6e-7 # 2-step with 8blk

cpuSecPerBlkStp = nblkx**ndim*cpuHrPerZnStp*3600. #0.38

if mri:
    dt = min(cfl*delXmin/cs, cfl * dx_mri / max(cs,4e4)) #9e-7 # for finest spacing 0.03 km, cs = 3.5e4 km/s
elif turbRes:
    dt = cfl*dx_turb/cs
else:
    dt = cfl*delXmin/cs

Nsteps = tmax/dt
print("Use rate =", cpuHrPerZnStp)
print("Nsteps, nblkx,", "dt =", dt)
print(int(Nsteps), nblkx)

Rmax = zeros(lref)
for i in range(lref):
    Rmax[i] = 2.**(i+1)*nblkx*delXmin / radiusFact

#Rmax1 = 2.*nblkx*delXmin / radiusFact
#Rmax2 = 4.*nblkx*delXmin / radiusFact
#Rmax3 = 8.*nblkx*delXmin / radiusFact

print("Effective resolution, % / degree")
print(1.5*delXmin/Rmax[0]*100., 1.5*delXmin/Rmax[0]*180./pi)
print("Minimum resolution, % / degree")
print(delXmin/Rmax[0]*100., delXmin/Rmax[0]*180./pi)
print("Maximum resolution, % / degree")
print(2.*delXmin/Rmax[0]*100., 2.*delXmin/Rmax[0]*180./pi)

maxBlks = zeros(lref)
print("lref, Rmax, dx, blks:")
maxBlks[0] = (2.*Rmax[0]/(delXmin*nblkx))**ndim
print(1, Rmax[0], delXmin, int(maxBlks[0]))
for i in range(1,lref):
    maxBlks[i] = (2.*Rmax[i]/(2.**i*delXmin*nblkx))**ndim - (2.*Rmax[i-1]/(2.**i*delXmin*nblkx))**ndim
    print(i+1, Rmax[i], delXmin*2.**i, int(maxBlks[i]))

#maxBlks2 = (2.*Rmax2/(2.*delXmin*nblkx))**ndim - (2.*Rmax1/(2.*delXmin*nblkx))**ndim
#print(Rmax2, int(maxBlks2))
#maxBlks3 = (2.*Rmax3/(4.*delXmin*nblkx))**ndim-(2.*Rmax2/(4.*delXmin*nblkx))**ndim
#print(Rmax3, int(maxBlks3))


avgBlks1 = 0.
avgBlks2 = 0.
avgBlks3 = 0.

avgBlks = zeros(lref)
if Rmax[0] < avShR:
    avgBlks[0] = maxBlks[0]
else:
    avgBlks[0] = (2.*avShR/(delXmin*nblkx))**ndim

for i in range(1,lref):
    if Rmax[i] < avShR:
        avgBlks[i] = maxBlks[i]
    elif Rmax[i-1] < avShR:
        avgBlks[i] = (2.*avShR/(2.**i*delXmin*nblkx))**ndim - (2.*Rmax[i-1]/(2.**i*delXmin*nblkx))**ndim


fac = zeros(lref)
for i in range(lref):
    if subCycle:
        fac[i] = 1.0 / 2.**i
    else:
        fac[i] = 1.0

if mri:
    pi43 = pi*4./3.
    # avgBlks[0] += (70./(  dx_mri*nblkx))**ndim - (50./(  dx_mri*nblkx))**ndim
    # avgBlks[1] += (90./(2*dx_mri*nblkx))**ndim - (70./(2*dx_mri*nblkx))**ndim
    # avgBlks[2] += (120./(4*dx_mri*nblkx))**ndim - (90./(4*dx_mri*nblkx))**ndim
    avgBlks[0] += pi43*(40./(  dx_mri*nblkx))**ndim - pi43*(15./(  dx_mri*nblkx))**ndim
    avgBlks[1] += pi43*(40./(2*dx_mri*nblkx))**ndim - pi43*(25./(2*dx_mri*nblkx))**ndim

if anteS:
    avgBlks[0] -= (50./(delXmin*nblkx))**ndim

if turbRes:
    avgBlks[0] -= (70./(delXmin*nblkx))**ndim

if trackShock:
    shockBlks = 4.*(2.**(ndim-1))*3.14159265*(avShR/delXmin/nblkx)**(ndim-1)
    print('shockBlks:', shockBlks)
    avgBlks[0] += shockBlks

if octant:
    avgBlks /= 8.0

# Now compute costs
cost = zeros(lref)
for i in range(lref):
    cost[i] = fac[i]*avgBlks[i]*Nsteps*cpuSecPerBlkStp/3600.

#cost1 = avgBlks1*Nsteps*cpuSecPerBlkStp/3600.
#cost2 = avgBlks2*Nsteps*cpuSecPerBlkStp/3600. * fac2
#cost3 = avgBlks3*Nsteps*cpuSecPerBlkStp/3600. * fac3

print ("Avg. Blks, cost")
for i in range(lref):
    print (i+1, avgBlks[i], cost[i]/1e6)

#print (avgBlks1, cost1/1e6)
#print (avgBlks2, cost2/1e6)
#print (avgBlks3, cost3/1e6)

print("Average num blocks, zones:")
print(int(sum(avgBlks)),int(sum(avgBlks))*nblkx**ndim)

totCost = sum(cost)
print("Cost (Mega core*hours):")
print(totCost/1.e6)

print("Number of runs at node counts (12hr/24hr):")
ranksPerNode = 8
nodes=8192
ranks = nodes*ranksPerNode
print(nodes, sum(avgBlks)/ranks, totCost/(12*nodes*16), totCost/(24*nodes*16))
nodes=4096
ranks = nodes*ranksPerNode
print(nodes, sum(avgBlks)/ranks, totCost/(12*nodes*16), totCost/(24*nodes*16))
nodes=2048
ranks = nodes*ranksPerNode
print(nodes, sum(avgBlks)/ranks, totCost/(12*nodes*16), totCost/(24*nodes*16))
