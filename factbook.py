import csv
file_name = 'happiness.csv'
with open(file_name) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	print(reader)