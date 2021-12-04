import pygal
from die import Die 

# create a D6 die
die_1 = Die(6)
die_2 = Die(6)

# create a list and append the rolls
results = [die_1.roll() * die_2.roll() for roll_num in range(1000)]

# analyse the total no of times the value appeared


max_sides = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(2,max_sides+1)]

# create a histogram based on the frequencies
hist = pygal.Bar()
hist.title = "A ROLL OF D6 DICE OVER 1000 TIMES"
hist.x_labels = [str(x) for x in range(1,max_sides+1)]
hist.x_title = "Value"
hist.y_title = "Frequency"

hist.add("D6 + D6",frequencies)
hist.render_to_file('dice_visual.svg')