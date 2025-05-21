import random

# List of possible choices
choices = ["rock", "paper", "scissors"]

# Get player input
player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

# Get computer choice
computer_choice = random.choice(choices)
print("Computer chose: {computer_choice}")

# Determine winner
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

