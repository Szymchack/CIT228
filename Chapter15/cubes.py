import matplotlib.pyplot as plt
cubed=[]
inputVal=[1,2,3,4,5]
for num in inputVal:
    cubed.append(num*num*num) 
ax1 = plt.subplot(1,2,1)    
ax1.plot(inputVal,cubed) 
plt.plot(inputVal, cubed,  marker='*', ls='-.', color='#B300B3',lw="3.0")
plt.title("Cubed Numbers")
plt.ylabel("Values Cubed")
plt.xlabel("Input Values")
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
plt.show()

