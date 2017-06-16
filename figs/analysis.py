import numpy as np
import io
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm


L = 1.0
k =2.*math.pi/L
V = 1.291

delx = []
delx2 = []
delx3 = []
delx4 = []
delx5 = []
delx6 = []
delx7 = []
delx8 = []
dissipation = []
dissipation2 = []
dissipation3 = []
dissipation4 = []
dissipation5 = []
dissipation6 = []
dissipation7 = []
dissipation8 = []
plot = []
plot2 = []
plot3 = []
plot4 = []
plot5 = []
plot6 = []
plot7 = []
plot8 = []

res = (8, 16, 32, 64, 128, 256, 512, 1024)
for r in res:
    filename = "sound_SparkFOGrk2_res"+str(r)+".dat"
    f = open(filename, "r")
    dx = 1./float(r)
    delx3.append(dx)
    time3, ekin3 = np.loadtxt(filename,usecols=(0,6),skiprows=2,unpack = True)
    logekin3 = [math.log(y) for y in ekin3]
    damping,b= np.polyfit(time3,logekin3,1)
    diss = -2.*damping/k
    dissipation3.append(diss)
    plot3.append(damping)

for r in res:
    filename = "sound_SparkTVDrk2_res"+str(r)+".dat"
    f = open(filename, "r")
    dx = 1./float(r)
    delx4.append(dx)
    time4, ekin4 = np.loadtxt(filename,usecols=(0,6),skiprows=2,unpack = True)
    logekin4 = [math.log(y) for y in ekin4]
    damping,b= np.polyfit(time4,logekin4,1)
    diss = -2.*damping/k
    dissipation4.append(diss)
    plot4.append(damping)

for r in res:
    filename = "sound_USM_res"+str(r)+".dat"
    f = open(filename, "r")
    dx = 1./float(r)
    delx5.append(dx)
    time5, ekin5 = np.loadtxt(filename,usecols=(0,6),skiprows=2,unpack = True)
    logekin5 = [math.log(y) for y in ekin5]
    damping,b= np.polyfit(time5,logekin5,1)
    diss = -2.*damping/k
    dissipation5.append(diss)
    plot5.append(damping)

for r in res:
    filename = "sound_SparkGLMrk2_res"+str(r)+".dat"
    f = open(filename, "r")
    dx = 1./float(r)
    delx6.append(dx)
    time6, ekin6 = np.loadtxt(filename,usecols=(0,6),skiprows=2,unpack = True)
    logekin6 = [math.log(y) for y in ekin6]
    damping,b= np.polyfit(time6,logekin6,1)
    diss = -2.*damping/k
    dissipation6.append(diss)
    plot6.append(damping)

res = (8, 16, 32, 64, 128)
for r in res:
    filename = "sound_SparkWeno5rk2_res"+str(r)+".dat"
    f = open(filename, "r")
    dx = 1./float(r)
    delx7.append(dx)
    time7, ekin7 = np.loadtxt(filename,usecols=(0,6),skiprows=2,unpack = True)
    logekin7 = [math.log(y) for y in ekin7]
    damping,b= np.polyfit(time7,logekin7,1)
    diss = -2.*damping/k
    dissipation7.append(diss)
    plot7.append(damping)

res = (8, 16, 32, 64, 128)
for r in res:
    filename = "sound_SparkMP5rk2_res"+str(r)+".dat"
    f = open(filename, "r")
    dx = 1./float(r)
    delx8.append(dx)
    time8, ekin8 = np.loadtxt(filename,usecols=(0,6),skiprows=2,unpack = True)
    logekin8 = [math.log(y) for y in ekin8]
    damping,b= np.polyfit(time8,logekin8,1)
    diss = -2.*damping/k
    dissipation8.append(diss)
    plot8.append(damping)


lndelx3 = [math.log(y) for y in delx3]
lndiss3 = [math.log(x) for x in dissipation3]
m,b = np.polyfit(lndelx3,lndiss3,1)
fit_tot = math.exp(b)*(math.pow(L,(m-1))/V)
print (m,fit_tot)

lndelx4 = [math.log(y) for y in delx4]
lndiss4 = [math.log(x) for x in dissipation4]
m,b = np.polyfit(lndelx4,lndiss4,1)
fit_tot = math.exp(b)*(math.pow(L,(m-1))/V)
print (m,fit_tot)

lndelx5 = [math.log(y) for y in delx5]
lndiss5 = [math.log(x) for x in dissipation5]
m,b = np.polyfit(lndelx5,lndiss5,1)
fit_tot = math.exp(b)*(math.pow(L,(m-1))/V)
print (m,fit_tot)

lndelx6 = [math.log(y) for y in delx6]
lndiss6 = [math.log(x) for x in dissipation6]
m,b = np.polyfit(lndelx6,lndiss6,1)
fit_tot = math.exp(b)*(math.pow(L,(m-1))/V)
print (m,fit_tot)


lndelx7 = [math.log(y) for y in delx7]
lndiss7 = [math.log(x) for x in dissipation7]
m,b = np.polyfit(lndelx7,lndiss7,1)
fit_tot = math.exp(b)*(math.pow(L,(m-1))/V)
print (m,fit_tot)

lndelx8 = [math.log(y) for y in delx8]
lndiss8 = [math.log(x) for x in dissipation8]
m,b = np.polyfit(lndelx8,lndiss8,1)
fit_tot = math.exp(b)*(math.pow(L,(m-1))/V)
print (m,fit_tot)

logdelx3 = [math.log10(y) for y in delx3]
logdiss3 = [math.log10(y) for y in dissipation3]
logdelx4 = [math.log10(y) for y in delx4]
logdiss4 = [math.log10(y) for y in dissipation4]
logdelx5 = [math.log10(y) for y in delx5]
logdiss5 = [math.log10(y) for y in dissipation5]
logdelx6 = [math.log10(y) for y in delx6]
logdiss6 = [math.log10(y) for y in dissipation6]
logdelx7 = [math.log10(y) for y in delx7]
logdiss7 = [math.log10(y) for y in dissipation7]
logdelx8 = [math.log10(y) for y in delx8]
logdiss8 = [math.log10(y) for y in dissipation8]

lgdelx = np.linspace(-5,-0.5,20)

plt.figure(1)
plt.title("Sound Wave, CFL=0.01")
plt.xlabel(r'log $\Delta$ x')
plt.ylabel(r'log (4/3 v$_{*}$+$\xi_{*}$)')
plt.scatter(logdelx5, logdiss5, color = 'k', label = 'USM')
y = [3.*dx+1.74547 for dx in lgdelx]
plt.plot(lgdelx, y, color = 'k')
plt.scatter(logdelx3, logdiss3, color = 'b', label = 'Spark FOG')
y = [dx+1.1313 for dx in lgdelx]
plt.plot(lgdelx,y, color = 'b')
plt.scatter(logdelx4, logdiss4, color = 'g', label = 'Spark TVD')
y = [2.*dx+1.46009 for dx in lgdelx]
plt.plot(lgdelx,y, color = 'g')
plt.scatter(logdelx6, logdiss6, color = 'r', label = 'Spark GLM')
y = [3.*dx+2.222 for dx in lgdelx]
plt.plot(lgdelx,y, color = 'r')
plt.scatter(logdelx7, logdiss7, color = 'c', label = 'Spark Weno5')
y = [5.*dx+1.69518 for dx in lgdelx]
plt.plot(lgdelx, y, color = 'c')
plt.scatter(logdelx8, logdiss8, color = 'm', label = 'Spark MP5')
y = [5.*dx+1.64244 for dx in lgdelx]
plt.plot(lgdelx,y, color = 'm')
plt.legend(loc = 'upper left',frameon = False)
plt.axis([-3.5,-0.5,-12,3])
plt.show()
