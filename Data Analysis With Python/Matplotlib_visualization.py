import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
#Plotting basic functions
x = np.linspace(0,2*np.pi)
y = np.sin(x)
plt.figure(1, figsize = (10,6))
plt.plot(x, y, 'r--')
plt.plot(x, np.log(x), 'm')
plt.plot(x, np.sqrt(x), 'bo')
plt.xlabel('RAD')
plt.ylabel('F(x)')
plt.title('Bayby Plots')
plt.legend(['Sine', 'Logarithmic', 'Sqrt'])
plt.show()
#Creating subplots
plt.figure(2, figsize = (10,10))
plt.suptitle('Example With Subplots')
plt.subplot(2,2,1)#plt.subplot(rows,columns,plot to refer to)
plt.plot(x,y)
plt.xlabel('Radians')
plt.ylabel('Sin(x)')
plt.title('SINX')
plt.legend(['Subplot_1'])
#####################
plt.subplot(2,2,2)#plt.subplot(rows,columns,plot to refer to)
plt.plot(x,np.log(x))
plt.xlabel('Radians')
plt.ylabel('Log(x)')
plt.title('LOGX')
plt.legend(['Subplot_2'])
#######################
#####################
plt.subplot(2,2,3)#plt.subplot(rows,columns,plot to refer to)
plt.plot(x,np.exp(x))
plt.xlabel('Radians')
plt.ylabel('Exp(x)')
plt.title('EXPX')
plt.legend(['Subplot_3'])
#####################
plt.subplot(2,2,4)#plt.subplot(rows,columns,plot to refer to)
plt.plot(x,np.sqrt(x))
plt.xlabel('Radians')
plt.ylabel('Sqrt(x)')
plt.title('SQRTX')
plt.legend(['Subplot_4'])
plt.show()
#Creating an interesting plot
butterfly = plt.figure(3,figsize = (10,6))
plt.plot(x,np.sqrt(x))
plt.plot(np.sqrt(x),x)
plt.plot(x, -np.sqrt(x))
plt.plot(-np.sqrt(x), x)
plt.plot(-x,np.sqrt(x))
plt.plot(np.sqrt(x),-x)
plt.plot(-x, -np.sqrt(x))
plt.plot(-np.sqrt(x), -x)
plt.xlim([-1,1])
plt.ylim([-2, 2])
plt.title('Simple butterFly')
plt.xlabel('X value')
plt.ylabel('Y value')
plt.tight_layout()
plt.show()
#Oblect Oriented Method
fig = plt.figure(4, figsize = (10,6))#main object
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel('Radians')
axes.set_ylabel('Sinx')
axes.set_title('Example Plot with OOP')
plt.show()
########################
fig1 = plt.figure(5, figsize = (10,6))
axes1 = fig1.add_axes([0.1,0.1,0.8,0.8])
axes1.plot(x,np.log(x),'r')
axes1.set_title('Large Plot')
axes2 = fig1.add_axes([0.3,0.2,0.4,0.3])#all the args are between 0 and 1
axes2.plot(x,np.exp(x))
axes2.set_title('Smaller Plot')
plt.show()
#fig,axes for subplots
fig,axes = plt.subplots(nrows = 1, ncols=2)
#the axes is an numpy array and we can iterate into them and plot functions
#for ax in axes:
#    ax.plot(x,1/x)
axes[0].plot(x,np.log(x),'r--')
axes[0].set_xlabel('X_Value')
axes[0].set_ylabel('Y_Value')
axes[0].set_title('Graph of logx')
axes[0].legend(['Log(x)'], loc = 'lower right')
axes[1].plot(np.log(x),x,'m--')
axes[1].set_xlabel('X_Value')
axes[1].set_ylabel('Y_Value')
axes[1].set_title('Graph of the inverse of logx')
axes[1].legend(['Inverse'], loc = 'upper left')
plt.show()
#dpi = dots per inch and you can commonly use the default value
#Save a figure(our butterfly)
butterfly.savefig('butterfly_plot.png')
#Should you like to chnage the width of the graph add in the plot the parameter linewidth which is by default = 1 more thick means more than one. Alpha is about the transparency of the graph.The marker marks every point of the x axis and the size of it can be handled by using markersize.Also the color can be regulated by the markerfacecolor and the boundary can be done by using markeredgecolor
#for only showing specific values of the x and y label we have this
#ax.set_xlim([0 ,1])
#ax.set_ylim([lower_bound, upper_bound])
#plt.scatter(x,y)
#plt.hist()
#plt.boxplot()
