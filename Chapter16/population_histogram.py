import matplotlib.pyplot as plt

population_changes=[77.7, 75.4, 78.8, 81.5, 78.5, 76.9]

plt.hist(population_changes, bins=3, color="#FFFF66")
plt.ylabel("States")
plt.xlabel("Changes")
plt.suptitle("Population changes to states")

plt.show()