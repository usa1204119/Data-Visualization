import csv
import matplotlib.pyplot as plt
from datetime import datetime
# get high temperatures from the file
file_name = 'death_valley_2014.csv'
with open(file_name) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	dates,highs,lows = [],[],[]
	for row in reader:
		try:
			current_date = datetime.strptime(row[0],"%Y-%m-%d")
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(current_date,'missing data')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)
# plot data
fig = plt.figure(dpi=90,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='purple',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='green',alpha=0.1)
# Format plot
plt.title('Daily High Temperature July\n Death Valley 2014')
plt.xlabel('',fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature[F]',fontsize=15)
plt.ylim(0,120)
plt.tick_params(axis='both',which='major',labelsize=10)

plt.savefig('death_valley_2014.png')

file_name_2 = 'sanfransico_2014.csv'
with open(file_name_2) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	dates,highs,lows = [],[],[]
	for row in reader:
		try:
			current_date = datetime.strptime(row[0],"%m/%d/%Y")
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(current_date,'missing data')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)
# plot data
fig = plt.figure(dpi=90,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='purple',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='green',alpha=0.1)
# Format plot
plt.title('Daily High Temperature July\n sanfransico_2014')
plt.xlabel('',fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature[F]',fontsize=15)
plt.ylim(0,120)
plt.tick_params(axis='both',which='major',labelsize=10)

plt.savefig('sanfransico_2014.png')