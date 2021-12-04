'''import matplotlib.pyplot as plt

# specifying the x values
input_values = [1,2,3,4,5]
# plotting a simple graph
squares = [1,4,9,16,25]
plt.plot(input_values,squares,linewidth=5)

# changing the label type and graph thickness
plt.title('Square Numbers',fontsize=14)
plt.xlabel('Values',fontsize=14)
plt.ylabel('Square',fontsize=14)

# Set the size of tick labels
plt.tick_params(axis='both',labelsize=14)
plt.show()

'''

import matplotlib.pyplot as plt

input_values= list(range(1,6))
squares = [1,4,9,16,25]

# defining x and y axis
plt.plot(input_values,squares,linewidth = 5)
plt.title('Square Numbers',fontsize=15)
plt.xlabel('Value',fontsize=15)
plt.ylabel('Square',fontsize=15)

# setting the label thickness
plt.tick_params(axis='both',which='major',labelsize=15)
plt.show()