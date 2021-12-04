import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'sitka_rainfall.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	for index,co in enumerate(header_row):
		print(index,co)
'''	
	dates,rainfalls = [],[]
	for row in reader:
		try:
			current_date = datetime.strptime(row[0],'%Y-%m-%d')
			rainfall = float(row[19])
		except ValueError:
			print(current_date,'missing data')
		else:
			dates.append(current_date)
			rainfalls.append(rainfall)

fig = plt.figure(dpi=80,figsize=(10,6))
plt.plot(dates,rainfalls,c='blue',alpha=0.5)
plt.fill_between(dates,rainfalls,facecolor='red',alpha=0.1)
plt.title('Rainfall 2015 \n Sitka ',fontsize=18)
plt.xlabel('',fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Rainfall (in)',fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.savefig('sitka_rainfall.png')
'''