from random import randint


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(f"{randint(1,self.sides)}")

diceSix=Dice()
x=1
while x<11:
	diceSix.roll_die()
	x+=1
	
print('----------')

diceTen=Dice(10)
y=1
while y<11:
	diceTen.roll_die()
	y+=1
print('----------')


z=1
diceTwenty=Dice(20)
while z<11:
	diceTwenty.roll_die()
	z+=1
print('----------')

