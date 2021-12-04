import matplotlib.pyplot as plt
from die import Die

die = Die(6)
results = [die.roll() for roll_num in range(1000)]
frequencies = [results.count(value) for value in range(1,die.num_sides+1)]
x_axis= list(range(1,7))

plt.xlabel('Value',fontsize=14)
plt.ylabel('Times Occured',fontsize=14)
plt.title('ROLL OF D6 DIE OVER 1000 TIMES')
plt.scatter(x_axis,frequencies)
plt.axis([0,7,0,200])
plt.tick_params(axis='both',labelsize=10)
plt.show()