'''from random import choice

class RandomWalk():
	""" A class to generate a random walk"""
	def __init__(self,num_points=5000):
		""" initalize all atrributes of random walk"""
		self.num_points = num_points

		# Start the walk at (0,0)
		self.x_values = [0]
		self.y_values = [0]


	def get_step(self):
		""" Set the direction and distance"""
		direction = choice([1,-1])
		distance = choice([0,1,2,3,4])
		step = direction * distance
		return step

	def fill_walk(self):
		""" Calculate all the points in the walk"""

		# keep taking steps until points are finished
		while len(self.x_values) < self.num_points:
			# set the direction and distance of walk

			x_step = self.get_step()
			y_step = self.get_step()

			
			# reject the moves that go nowhere
			if x_step == 0 and y_step == 0:
				continue

			# calcualte the next x and y values
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step

			self.x_values.append(next_x)
			self.y_values.append(next_y)



'''
from random import choice

class Random():
	""" A class to generate random walk"""
	def __init__(self,num_sides=5000):
		""" Initalize the walk attributes"""
		self.num_sides = num_sides

		# All walks starts at 0,0
		self.x_axis = [0]
		self.y_axis = [0]

	def fill_walk(self):
		""" Calculate all the points in the walk"""
		# Determine which direction and how far to go.
		while len(self.x_axis) < self.num_sides:
			x_direction = choice([1,-1])
			x_distance = choice(list(range(0,5)))
			x_step = x_direction * x_distance

			y_direction = choice([1,-1])
			y_distance = choice(list(range(0,5)))
			y_step = y_direction * y_distance
			
			# Rejects moves that go nowhere

			next_x = self.x_axis[-1] + x_step
			next_y = self.y_axis[-1] + y_step

			# calculate the next x and y values
			self.x_axis.append(next_x)
			self.y_axis.append(next_y)
			


