import matplotlib.pyplot as plt

input_values = list(range(1,5001))
cubes = [x**3 for x in input_values]

# defining the values for x and y axis
plt.scatter(input_values,cubes,c=cubes,cmap=plt.cm.Reds,s=20)

# labeling the axes and giving a title to chart
plt.title('Cubic Numbers',fontsize=14)
plt.xlabel('Values',fontsize=14)
plt.ylabel('Cubes',fontsize=14)

# set the size of tick labels
plt.tick_params(axis='both',which='major',labelsize=14)

# set the axis size
plt.axis([0,5400,0,134651000000])
plt.savefig('cubes.png',bbox_inches='tight')