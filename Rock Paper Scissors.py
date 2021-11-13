from random import randint

choices = ["Rock", "Paper", "Scissors"]

computer_choice = choices[randint(0,2)]

player_choice = input("Rock, Paper, Scissors? ")

if player_choice == computer_choice:
    print("Bot choice: ", computer_choice)
    print("Your choice: ", player_choice)
    print("Result: Tie!")
elif player_choice == "Rock":
    if computer_choice == "Paper":
        print("Bot choice: ", computer_choice)
        print("Your choice: ", player_choice)
        print("Result: You lose!")
    else:
        print("Bot choice: ", computer_choice)
        print("Your choice: ", player_choice)
        print("Result: You win!")
elif player_choice == "Paper":
    if computer_choice == "Scissors":
        print("Bot choice: ", computer_choice)
        print("Your choice: ", player_choice)
        print("Result: You lose!")
    else:
        print("Bot choice: ", computer_choice)
        print("Your choice: ", player_choice)
        print("Result: You win!")
elif player_choice == "Scissors":
    if computer_choice == "Rock":
        print("Bot choice: ", computer_choice)
        print("Your choice: ", player_choice)
        print("Result: You lose!")
    else:
        print("Bot choice: ", computer_choice)
        print("Your choice: ", player_choice)
        print("Result: You win!")
else:
    print("The choice is not valid!")
