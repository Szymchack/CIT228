import matplotlib.pyplot as plt


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Alaska', 'Hawii', 'Maine', 'Michigan', 'Montana', 'Wyoming'
population = [78.4, 78.8, 81.5, 78.5, 78.6, 76.9]
explode = (0, 0, .1, 0, 0, 0)  # only "explode" the 1st wedge
wedgeColors=('#ff6680','#9966ff','#6699ff','#66ff99','#ffa64d', '#ffff66')

fig1, ax1 = plt.subplots()
ax1.pie(population, explode=explode, labels=labels, autopct='%3.1f%%', shadow=True, startangle=1, colors=wedgeColors)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.suptitle("Population expansion from 2018-2019")

plt.show()