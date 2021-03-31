import matplotlib.pyplot as plt
michigan=[]
inputVal=[9986857, 7842924,	78.5]
for num in inputVal:
    michigan.append(num-num) 
ax1 = plt.subplot(1,2,1)    
ax1.plot(inputVal,michigan) 
plt.plot(inputVal, michigan,  marker='*', ls='-.', color='#B300B3',lw="3.0")
plt.title("Michigan")
plt.ylabel("2019")
plt.xlabel("2018")
plt.grid()
power=[]
inputVal=[1,2,3,4,5]
for num in inputVal:
    power.append(num**2) 
ax2 = plt.subplot(1,2,2)    
ax2.plot(inputVal,power) 
plt.plot(inputVal,power)
plt.title("Numbers Raised")
plt.ylabel("Second Power")
plt.xlabel("Input Values")
plt.grid()
plt.suptitle("Fun with Numbers",color='#00cc00',fontfamily="Segoe Script", fontsize="36")
plt.subplots_adjust(top=.8,wspace=1)
plt.style.use("seaborn-dark-palette")
ax2.plot(inputVal,power,color="#990000",lw="2",marker="^")
plt.title("Numbers Raised", color="#4d0033")  
plt.show()

