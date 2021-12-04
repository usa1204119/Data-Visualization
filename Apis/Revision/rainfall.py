import csv
import matplotlib.pyplot as plt
from datetime import datetime
# get high temperatures from the file
file_name = 'sitka_weather_2014.csv'
with open(file_name) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	dates,rainfalls = [],[]
	for row in reader:
		try:
			current_date = datetime.strptime(row[0],"%Y-%m-%d")
			rainfall = float(row[19])
			
		except ValueError:
			print(current_date,'missing data')
		else:
			dates.append(current_date)
			rainfalls.append(rainfall)
			
	# plot data
fig = plt.figure(dpi=90,figsize=(10,6))
plt.plot(dates,rainfalls,c='red',alpha=0.5)
plt.fill_between(dates,rainfalls,facecolor='green',alpha=0.1)
# Format plot
plt.title('Rainfall 2014 \n Sitka Alaska')
plt.xlabel('',fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature[F]',fontsize=15)

plt.tick_params(axis='both',which='major',labelsize=10)

plt.savefig('rainfall_sitka.png')