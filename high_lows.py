'''import csv
import matplotlib.pyplot as plt
from datetime import datetime

# get the high temperatures of sitka
file_name = 'sitka_weather_2014.csv'
with open(file_name) as f:
	reader = csv.reader(f)
	# reading the next line that is first line
	header_row = next(reader)
	# creating the index 
	# enumerate creates the index
	#for index,column_header in enumerate(header_row):
	#	print(index,column_header)
	dates,highs,lows = [],[],[]
	for row in reader:
		current_date = datetime.strptime(row[0],'%Y-%m-%d')
		dates.append(current_date)
		high = int(row[1])
		highs.append(high)
		low = int(row[3])
		lows.append(low)
# create a plot
fig = plt.figure(dpi=80,figsize=(10,6))
plt.plot(dates,highs,c='green')
plt.plot(dates,lows,c='pink')
# format plot
plt.title('Daily High,Low Temperatures, 2014',fontsize=24)
plt.xlabel('',fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)',fontsize=14)

plt.tick_params(axis='both',which='minor',labelsize='12')
plt.show()
'''
import csv
import matplotlib.pyplot as plt
from datetime import datetime
file_name = 'sitka_weather_2014.csv'
with open(file_name) as f:
	# Get high temperatures of file
	reader = csv.reader(f)
	header_row = next(reader)
	
	dates,highs,lows = [],[],[]
	for row in reader:
		try:
			current_date = datetime.strptime(row[0],'%Y-%m-%d')
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(current_date,'missing data')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

# Format plot
fig = plt.figure(dpi=80,figsize=(10,8))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='green',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='purple',alpha=0.1)
plt.title('Daily High and Low Temperatures \n Sitka-2014',fontsize=24)
plt.xlabel('',fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)',fontsize=14)
plt.ylim(10,120)
plt.tick_params(axis='both',which='minor',labelsize='12')
plt.savefig('sitka.png')