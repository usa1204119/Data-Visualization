import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get dates, high, and low temperatures from file for Death Valley and Sitka.
filename = 'death_valley.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:          
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    
# Plot data.
fig = plt.figure(dpi=80, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=16)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=14)
plt.ylim(10, 120)
plt.savefig('death_valley.png')
# Get dates, high, and low temperatures from file for Death Valley and Sitka.
filename2 = 'sitka_weather_2014.csv'
with open(filename2) as f2:
    reader = csv.reader(f2)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:          
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    
# Plot data.
fig = plt.figure(dpi=80, figsize=(10, 6))
plt.plot(dates, highs, c='green', alpha=0.5)
plt.plot(dates, lows, c='yellow', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.1)

# Format plot.
title = "Daily high and low temperatures - 2014\nSitka, AK"
plt.title(title, fontsize=16)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=14)
plt.ylim(10, 120)

plt.savefig('sitka.png')
                      