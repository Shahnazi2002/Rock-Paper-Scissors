from random import randint

choices = ["Rock", "Paper", "Scissors"]

bot = choices[randint(0,2)]

player = input("Rock, Paper, Scissors? ")

if player == bot:
    print("Bot choice: ", bot)
    print("Your choice: ", player)
    print("Result: Tie!")
elif player == "Rock":
    if bot == "Paper":
        print("Bot choice: ", bot)
        print("Your choice: ", player)
        print("Result: You lose!")
    else:
        print("Bot choice: ", bot)
        print("Your choice: ", player)
        print("Result: You win!")
elif player == "Paper":
    if bot == "Scissors":
        print("Bot choice: ", bot)
        print("Your choice: ", player)
        print("Result: You lose!")
    else:
        print("Bot choice: ", bot)
        print("Your choice: ", player)
        print("Result: You win!")
elif player == "Scissors":
    if bot == "Rock":
        print("Bot choice: ", bot)
        print("Your choice: ", player)
        print("Result: You lose!")
    else:
        print("Bot choice: ", bot)
        print("Your choice: ", player)
        print("Result: You win!")
else:
    print("The choice is not valid!")