import random #you can import only randint by doing "from random import randint"

player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:
	print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
	print("Rock....")
	print("Paper....")
	print("Scissors....")


	player = input("Player 1, make your move: ").lower()
	if player == "quit" or player == "q":
		break
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
			player_wins += 1
		elif computer == "paper":
			print("Computer Wins!")
			computer_wins += 1
	elif player == "paper":
		if computer == "rock":
			print("Player Wins!")
			player_wins += 1
		elif computer == "scissors":
			print("Computer Wins!")
			computer_wins += 1
	elif player == "scissors":
		if computer == "rock":
			print("Computer Wins!")
			computer_wins += 1
		elif computer == "paper":
			print("Player Wins!")
			player_wins += 1
	else:
		print("Please enter a valid move")

print(f"FINAL SCORES.........Player Score: {player_wins} Computer Score: {computer_wins}")

