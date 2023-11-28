import random

def game():
    choices = ["rock", "scissors", "paper", "lizard", "Spock"]

    computer_choice = random.choice(choices)

    print("Choose your option:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")

    player_choice_index = int(input()) - 1
    player_choice = choices[player_choice_index]

    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
        return 0
    elif (
        (player_choice == "rock" and (computer_choice == "scissors" or computer_choice == "lizard")) or
        (player_choice == "scissors" and (computer_choice == "paper" or computer_choice == "lizard")) or
        (player_choice == "paper" and (computer_choice == "rock" or computer_choice == "Spock")) or
        (player_choice == "lizard" and (computer_choice == "paper" or computer_choice == "Spock")) or
        (player_choice == "Spock" and (computer_choice == "rock" or computer_choice == "scissors"))
    ):
        print("You win!")
        return 1
    else:
        print("You lose!")
        return -1

score = 0
question = "yes"
while question.lower() == "yes":
    result = game()
    score += result
    print(f"Your current score: {score}")
    question = input("Do you want to play again? (yes/no): ")

print("Thanks for playing! Your final score:", score)