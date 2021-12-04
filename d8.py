import pygal
from die import Die 

die_1 = Die(8)
die_2 = Die(8)

results = [die_1.roll() + die_2.roll() for roll_num in range(5000)]

max_results = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2,max_results+1)]

hist = pygal.Bar()
hist.title = "Roll of d8 dice over 5000 times"
hist.x_labels = [str(x) for x in range(2,max_results+1)]
hist.x_title = 'Value'
hist.y_title = 'Frequency of Value'

hist.add("D8+D8",frequencies)
hist.render_to_file('d8.svg')