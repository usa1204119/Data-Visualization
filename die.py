from random import randint

class Die():
	""" A simple model of Die"""
	def __init__(self,num_sides=8):
		""" Make a D6 sided die"""
		self.num_sides = num_sides

	def roll(self):
		""" Roll a die """
		return randint(1,self.num_sides)
