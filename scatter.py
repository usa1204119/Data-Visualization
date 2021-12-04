import matplotlib.pyplot as plt

plt.scatter(2,4,s=200)
plt.title('Square Numbers',fontsize=24)
plt.xlabel('Squares',fontsize=14)
plt.ylabel('Values',fontsize=14)

# set the chart width 
plt.tick_params(axis='both',labelsize=14)

plt.show()