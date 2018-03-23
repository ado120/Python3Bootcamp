import random

random_number = random.randint(1,10)  # numbers 1 - 10

# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!

while True:
	USER_GUESS  = int(input("Input a number from 1 to 10: "))
	if USER_GUESS < random_number:
		print("TOO LOW")
	elif USER_GUESS > random_number:
		print("TOO HIGH!")
	else:
		print("YOU WIN!!")
		play_again = input("Do you want to play again? (y/n) ")
		if play_again == "y":
			random_number = random.randint(1,10)  # numbers 1 - 10
			USER_GUESS = None
		else:
			print("Thank you for playing.")
			break
