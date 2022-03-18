
import random
x = random.randint(1,10)
y = random.randint(1,100)
z = random.randint(1,1000)

mode = input ("Would you like to pick easy ,hard ,or insane?: ")
if mode == "easy":
	for i in range(1,5):
		user_input = input("Pick a number between 1-10: ")
		if int(user_input) == x:
			print("You were correct!" + " Here is your cake [***]")
		if int(user_input) > x:
			print("You were too high!")
		if int(user_input) < x:
			print("You were too low!")
	print("The number was " + str(x))
if mode == "hard":
	for i in range(1,10):
		user_input = input("Pick a number between 1-100: ")
		if int(user_input) == y:
			print("You were correct!" + " Here is your cake [*********] and money $$$$")
		if int(user_input) > y:
			print("You were too high!")
		if int(user_input) < y:
			print("You were too low!")
	print("The number was " + str(y))
if mode == "insane":
	for i in range(1,10):
		user_input = input("Pick a number between 1-1000: ")
		if int(user_input) == z:
			print("You were correct!" + " Here is your cake [**************] and money $$$$$$$ ")
		if int(user_input) > z:
			print("You were too high!")
		if int(user_input) < z:
			print("You were too low!")
	print("The number was " + str(z))
