import matplotlib
matplotlib.use('TkAgg')
import os   #to work with files and directories
import pandas as pd    #to work with dataframes
import matplotlib.pyplot as plt
import numpy as np      #get the code from practical instruction
os.chdir("/Users/yefen/IBI1_2021-22/Practical7")
covid_data = pd.read_csv("full_data.csv")
#get code from practical instruction. To show the first and third columns from rows 10-20
print(covid_data.iloc[10:21,[1,3]])
print(covid_data.loc[0: ,"location"]) #just read the "location" column, but all rows from data
my_index=[]
print(covid_data.loc[my_index,"total_cases"])
for i in range(7996):  #set cycle
    if covid_data.iloc[i,1]=="Afghanistan":  #I get help from my classmate Xu Ziyi
        my_index.append(True)  #use boolean
    else:
        my_index.append(False)
print(covid_data.loc[my_index,"total_cases"])
#  select only data, new cases and new death of China
my_row=[]
for x in range(7996):
    if covid_data.iloc[x,1]=="China":
        my_row.append(True)
    else:
        my_row.append(False)
print(covid_data.loc[my_row,"total_cases"])
china_new_data= covid_data.iloc[1454:1546,[0,2,3]]#make a new object only store the data on new cases and death for China
info=china_new_data.describe()
print(info)  #print mean of nea cases and new death cases
# use numpy to cauclate the mean of new cases and new death cases
c=sum(china_new_data.iloc[0: ,1])/len(china_new_data.iloc[0: ,1])
print('the mean of new cases is',c)
d=sum(china_new_data.iloc[0: ,2])/len(china_new_data.iloc[0: ,2])
print('the mean of new death is', d)
#draw the boxplot of new cases and new death cases in China
china_new_cases=china_new_data.iloc[0: ,1]
china_new_death=china_new_data.iloc[0: ,2]
dt = pd.DataFrame({"new_cases": china_new_cases, "new_death_cases": china_new_death})
plt.ylabel('number')
plt.xlabel('x')
plt.boxplot(x=dt.values,labels=dt.columns)
plt.show()
# draw the plot of the data over time,and set different color and dot shape of each plot
china_dates=(china_new_data.iloc[0: ,0])
plt.ylabel('number')
plt.xlabel('date')
plt.title('comparing new cases and new deaths in China')
plt.plot(china_dates,china_new_cases,'bo',label='new cases') #"r+" and "b+" are the color of the points, "bo" is the shape of plot pionts
plt.plot(china_dates,china_new_death,'r+',label='new deaths')
plt.xticks(china_dates.iloc[0:len(china_dates):6],rotation=-20) #can see the date more clearly
plt.legend()
plt.show()
# draw the total number of deaths and cases in Canda
my_g=[]
for x in range(7996):
    if covid_data.iloc[x,1]=="Canada":
        my_g.append(True)
    else:
        my_g.append(False)
print(covid_data.loc[my_g,"total_cases"])
Canda_new_data= covid_data.iloc[1284:1376,[0,4,5]]
total_cases=Canda_new_data.iloc[0: ,1]  #set the number of total cases
total_deaths=Canda_new_data.iloc[0: ,2] # set the number of total death
# plot the total number of deaths and cases in Canda
plt.ylabel('number')
plt.xlabel('date')
plt.title('comparing total cases and total deaths in Canda')
Canda_dates=Canda_new_data.iloc[0: ,0]
plt.plot(Canda_dates,total_cases,label='total cases')
plt.plot(Canda_dates,total_deaths,label='total deaths')
plt.xticks(Canda_dates.iloc[0:len(china_dates):6],rotation=-20)
plt.legend()
plt.show()

