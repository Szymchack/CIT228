import matplotlib.pyplot as plt  
import numpy as np 


population_19 = [731545,
1415872,
1344212,
9986857,
1068778,
578759
]
population_18=[551562,1116004, 1095370, 7842924, 840190
,445025]
population_total=[75.4, 78.8, 81.5, 78.5, 78.6,76.9]
state = ["Alaska", "Hawaii", "Maine", "Michigan", "Montana", "Wyoming"]
barWidth=.25

#position of bar on x axis
br1 = np.arange(len(state)) 
br2 = [x + barWidth for x in br1] 
br3 = [x * barWidth for x in br2] 

plt.xticks([r + barWidth for r in range(len(state))],state) 

# creating the bar plot 
plt.bar(br1, population_19, color = '#9580ff', width=barWidth, label="2019") 
plt.bar(br2, population_18, color='#80bfff',  width=barWidth, label="2018")
plt.bar(br3,population_total, color= '#66ffff', width=barWidth,  label="Percent")
  
plt.ylabel("Change") 
plt.xlabel("State") 
plt.title("Comparison of growth per state.") 
plt.legend(loc="best")
plt.show() 