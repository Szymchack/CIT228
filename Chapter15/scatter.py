import matplotlib.pyplot as plt
from numpy.random import random

days = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

tempsJune = [99,86,87,88,111,86,103,87,94,78,77,85,88,82,85,85,88,89,89,90,89,78,80,81,82,83,82,83,84,85]
tempsJuly = [100,105,84,105,90,99,90,95,94,100,79,112,99,100,101,100,99,97,96,98,97,92,89,88,88,86,87,85,86,88]
tempsJan = [10,8,15,11,23,33,23,44,30,32,34,35,34,35,22,32,34,35,34,35,32,34,35,34,35,32,34,35,34,35,]
tempsFeb=[19,21,18,22,23,25,29,30,33,35,55,56,60,55,58,55,56,52,51,50,50,49,48,48,45,44,42,41,40,41]
tempRange=[0,20,40,60,100]

"""plt.scatter(tempsJune, days, color='#ffbb99',label="June")#color for Lisa
plt.scatter(tempsJuly, days, color='#ff5500',label="July")# Color for Lisa
plt.scatter(tempsJan, days, color='#33ffff',label="Jan")
plt.scatter(tempsFeb, days, color='#B3E5FF',label="Feb")"""

plt.scatter(tempsJune,tempRange,c=tempRange,cmap=plt.cm.PiYG)
plt.scatter(tempsJuly,tempRange,c=tempRange,cmap=plt.cm.PiYG)
plt.scatter(tempsJan,tempRange,c=tempRange,cmap=plt.cm.coolwarm)
plt.scatter(tempsFeb,tempRange,c=tempRange,cmap=plt.cm.coolwarm)

plt.ylabel('#Days')
plt.xlabel('Temps')
plt.title('Temperature Variation')
plt.subtitle('June/July vs Jan/Feb')
#plt.legend(loc='lower center', ncol=1, fontsize=8)

plt.grid()
plt.show() 