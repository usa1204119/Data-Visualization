'''import matplotlib.pyplot as plt

# define x,y axis and size of the point
x_axis = list(range(1,1001))
y_axis = [x**2 for x in x_axis]
# define x,y values and set custom colors and add cmap attribute to 
# show the dim effect and set the edgecolor and size
plt.scatter(x_axis,y_axis,c=y_axis,cmap=plt.cm.Greens,edgecolor='none',s=20)

# set chart title and label axis
plt.title('Square Numbers',fontsize=14)
plt.xlabel('Values',fontsize=14)
plt.ylabel('Square',fontsize=14)

# Set the size of tick labels 
plt.tick_params(axis='both',which='major',labelsize=14)
# set the both axis length
plt.axis([0,1100,0,1100000])

# first argument saves the file and second argument trims the extra whitespace
plt.savefig('squares_plot.png',bbox_inches='tight')'''

import matplotlib.pyplot as plt
x_axis = list(range(1,1001))
y_axis = [x**2 for x in x_axis]
plt.scatter(x_axis,y_axis,c=y_axis,cmap=plt.cm.Reds,edgecolor='none',s=100)
plt.title('Square Numbers',fontsize=14)
plt.xlabel('Values',fontsize=14)
plt.ylabel('Square',fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.axis([0,1100,0,1100000])
plt.savefig('revision.png',bbox_inches='tight')

