from random import randint

figure = randint(1, 100)
counter = 1
while True:
	while  True:
		try:
			proba = int(input("Your choice: "))
			break
		except ValueError:
			print("Please, try again")
		
	if proba == figure:
		print("You won! You made ", counter, "attempts")
		break
	else:
		counter += 1
	if proba > figure:
		print("Less")
	else:
		print("More")

