import numpy as np
import math
import random
import matplotlib.pyplot as plt
import pylab
from matplotlib.ticker import(MultipleLocator,AutoMinorLocator)
#1
Nu = 7
Q = 4
x = np.linspace(0,10,50)
f = (1/Q*math.sqrt(2*math.pi))*math.e**(-(((x-Nu)**2))/Q**2)
f2 = f*1.2
#Построение графика
ax = plt.subplot()
plt.title("Два графика",fontsize = 16)
plt.xlabel("x",fontsize = 14)
plt.ylabel("y1,y2",fontsize = 14)
plt.grid()
plt.grid(which = 'minor',linestyle = '--',color = 'green',linewidth = 0.5)
ax.plot(x,f,label = "f(x)",color = 'red',linestyle = '-.')
ax.plot(x,f2,label = "f2(x)",color = 'blue',linestyle = ':')
ax.legend(loc = 'upper left')
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
plt.show()


#2
fig = plt.figure()
n = 1000
t = np.linspace(0,10,n)
plt.title('Белый шум')
for i in range(1,11):
    ax = fig.add_subplot(10,1,i)
    ax.plot(t,[random.uniform(-1,1)for i in range(n)],color = 'green')
    ax.grid()
plt.show()

#3
day = ['eat','relaxation','sleep','work']
time = [3,3,8,10]
plt.bar(day,time)
plt.title('Time distribution',fontsize = 16)
plt.xlabel('Classes',fontsize = 14)
plt.ylabel('Hours',fontsize = 14)
plt.grid()
plt.show()


#4
xl = np.linspace(-10,10,100)
yl = np.linspace(-10,10,100)
x,y = np.meshgrid(xl,yl)
f = x**2 - 3*x*y + y**2 + x + 2*y + 5 
ax = plt.subplot()
plt.title("График",fontsize = 16)
plt.xlabel("x",fontsize = 14)
plt.ylabel("y",fontsize = 14)
plt.grid(True)
ax.contour(x,y,f,[0])
ax.legend(loc = 'upper left')
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
plt.show()


#5
xlist = np.linspace(0,6.5,50)
ylist = np.linspace(0,6.5,50)
x,y = np.meshgrid(xlist,ylist)
zl = np.sin(x*y)
fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')
ax.plot_surface(x,y,zl,cmap = 'inferno')
plt.title("sinxy",fontsize = 16)
plt.xlabel("x",fontsize = 14)
plt.ylabel("y",fontsize = 14)
plt.grid()
plt.show()




