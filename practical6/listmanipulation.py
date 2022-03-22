marks=[45,36,86,57,53,92,64,45]
sorted(marks) # returns sorted marks
marks=sorted(marks) # chenge the list to the sorted marks
print(marks) # show the sorted marks
sum = 0
for i in range(len(marks)):  #get Rob's average score 
 sum += marks[i]
b= sum/len(marks)
print('the average mark is', b)
if b >= 60:      #compare the average score to the pass mark of 60%
    print('the average mark is higher than the pass mark')
else:
    print('the average mark is lower than the pass mark')
import matplotlib #import the plot
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
plt.boxplot(marks)             #draw the plot
plt.xlabel('x')   #set the x axis
plt.ylabel('marks') #set y axis
plt.show()   #show the plot
