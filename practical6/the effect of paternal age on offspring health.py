import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
x=np.array([30,35,40,45,50,55,60,65,70,75]) # set the variable of the requested paternal age
y=np.array([1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]) # set the variable of risk for congenital heart disease
fig = plt.figure()
ax1=fig.add_subplot(111)
ax1.set_title('the effect of paternal age on offspring health')  # set the plot title
plt.xlabel('paternal_age') # set the label of x axis
plt.ylabel('chd') #set thelabel of y axis
plt.xlim(xmax=80,xmin=20) # set x axis range
plt.ylim(ymax=2,ymin=1)  # set y axis range
ax1.scatter(x,y, c = 'r', marker = 'o', label='paternal_age') 
plt.legend()
plt.show() #print the plot
