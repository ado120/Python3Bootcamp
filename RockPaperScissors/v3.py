import random #you can import only randint by doing "from random import randint"


print("Rock....")
print("Paper....")
print("Scissors....")


player = input("Player 1, make your move: ").lower()
rand_num = random.randint(0,2)
if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else: 
	computer = "scissors"
print(f"Computer plays {computer}")


if player == computer:
	print("It's a tie!")
elif player == "rock":
	if computer == "scissors":
		print("Player Wins!")
	elif computer == "paper":
		print("Computer Wins!")
elif player == "paper":
	if computer == "rock":
		print("Player Wins!")
	elif computer == "scissors":
		print("Computer Wins!")
elif player == "scissors":
	if computer == "rock":
		print("Computer Wins!")
	elif computer == "paper":
		print("Player Wins!")
else:
	print("Please enter a valid move")

