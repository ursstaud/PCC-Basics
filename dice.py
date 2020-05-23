from random import randint

class Dice:
	def __init__(self, sides):
		self.sides = sides

	def roll_die(self):
		roll = randint(1,self.sides)
		print(roll)

dice1 = Dice(6)
dice1.roll_die()

dice2 = Dice(10)
dice2.roll_die()

dice3 = Dice(20)
dice3.roll_die()