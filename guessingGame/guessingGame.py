import random

random_number = random.randint(1,10)  # numbers 1 - 10

# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!

USER_GUESS  = None

#or guess = int(guess)

# if USER_GUESS == random_number:
# 	print("YOU GOT IT!")
# elif USER_GUESS > random_number:
# 	print("TOO HIGH")
# else:
# 	print("TOO LOW")

while USER_GUESS != random_number:
	USER_GUESS  = int(input("Input a number from 1 to 10: "))
	if USER_GUESS < random_number:
		print("TOO LOW")
	elif USER_GUESS > random_number:
		print("TOO HIGH!")
	else:
		print("YOU WIN!!")

print(random_number)