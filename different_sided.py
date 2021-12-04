import pygal
from die import Die 

# create a D6 die
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)


# create a list and append the rolls
results = []

for roll_num in range(50000):
	result =  die_1.roll() + die_2.roll() + die_3.roll() 
	results.append(result)

# analyse the total no of times the value appeared
max_sides = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = []
for value in range(3,max_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# create a histogram based on the frequencies
hist = pygal.Bar()
hist.title = "A ROLL OF THREE D6 DIE OVER 50000 TIMES"
hist.x_labels = [str(x) for x in range(3,max_sides+1)]
hist.x_title = "Value"
hist.y_title = "Frequency"

hist.add("D6 + D10",frequencies)
hist.render_to_file('diffdice_visual.svg')