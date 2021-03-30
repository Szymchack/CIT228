import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'Chapter16/Copper_Harbor.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #Get dates and high temperatures from this filename
    dates, highs, lows  = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
#Plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(dates, highs, c='#9104a6')
ax.scatter(dates, lows, c='#0fedfd')

#Format plot
plt.suptitle("June-August, 2020")
plt.title("Copper Harbor Temperatures", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
