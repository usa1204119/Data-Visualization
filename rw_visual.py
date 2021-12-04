'''import matplotlib.pyplot as plt
from random_walk import RandomWalk

# making new walk as long as while loop is active
while True:
	# make a random walk and plot the points

	rw =RandomWalk(5000)
	rw.fill_walk()

	# set the size of the plotting windows
	plt.figure(dpi=128,figsize=(10,6))

	point_numbers = list(range(rw.num_points))
	#  if scatter then
	plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Reds,s=2)

	# if line then 
	#plt.plot(rw.x_values,rw.y_values,linewidth=2,zorder=1)

	# emphasize the first and last  point
	plt.scatter(0,0,c='blue',s=15,zorder=2)
	plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=15,zorder=2)
	
	plt.axis('off')
	plt.show()
	
	keep_running = input("Make another walk? (y/n) : ")
	if keep_running == 'n':
		break

'''

import matplotlib.pyplot as plt
from random_walk import Random
# keep the loop running
while True:
	rw = Random(5000)
	rw.fill_walk()

	plt.scatter(rw.x_axis,rw.y_axis,c=rw.y_axis,cmap=plt.cm.Purples,s=15)
	
	# set the first and last point differently
	plt.scatter(0,0,c='green',s=45)
	plt.scatter(rw.x_axis[-1],rw.y_axis[-1],c='red',s=45)
	# off the axis
	plt.axis('off')

	plt.show()

	keep_running = input("Make another walk(y/n)?")
	if keep_running == 'n':
		break