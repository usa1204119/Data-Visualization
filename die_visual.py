import pygal
from die import Die 

# create a D6 die
die = Die()

# create a list and append the rolls
results = [die.roll() for roll_num in range(1,1000)]


# analyse the total no of times the value appeared

frequencies = [results.count(value) for value in range(1,die.num_sides+1)]

# create a histogram based on the frequencies
hist = pygal.Bar()
hist.title = "A ROLL OF D6 DIE OVER 100 TIMES"
hist.x_labels = [str(x) for x in range(1,die.num_sides+1)]
hist.x_title = "Value"
hist.y_title = "Frequency"

hist.add("D6",frequencies)
hist.render_to_file('data_visual.svg')