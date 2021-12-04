import csv
file_name = 'education.csv'
with open(file_name) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	