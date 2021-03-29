import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'PNG', 'JPEG', 'SVG', 'GIF', 'Other'
usedSite = [376.0, 348.0, 153.0, 104.0, 19.0]
explode = (0, .1, 0, 0, 0)  # only "explode" the 1st wedge
wedgeColors=('#4DFFE1','#4DFFA6','#4DFF4D','#4DA6FF', '#4D4DFF')

fig1, ax1 = plt.subplots()
ax1.pie(usedSite, explode=explode, labels=labels, autopct='%3.1f%%', shadow=True, startangle=1, colors=wedgeColors)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.suptitle("Most popular Graphic Formats on the Web")

plt.show()