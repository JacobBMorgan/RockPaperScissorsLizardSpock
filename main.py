import random

playerWinCount = 0
computerWinCount = 0

while True:
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    print("4. Lizard")
    print("5. Spock")

    computerChoice = random.randint(1, 5)
    playerChoice = int(input("Make a selection: "))
    if playerChoice != 1 and playerChoice != 2 and playerChoice != 3 and playerChoice != 4 and playerChoice != 5:
        print("Invalid selection! Try again.")
        continue

    # Draw condition
    if playerChoice == computerChoice:
        if playerChoice == 1:
            print("You both threw Rock! Draw!")
        if playerChoice == 2:
            print("You both threw Paper! Draw!")
        if playerChoice == 3:
            print("You both threw Scissor! Draw!")
        if playerChoice == 4:
            print("You both threw Lizard! Draw!")
        if playerChoice == 5:
            print("You both threw Spock! Draw!")

    # Rock conditions
    elif playerChoice == 1 and computerChoice == 2:
        print("The computer throws paper, covering your rock! You lose!")
        computerWinCount = computerWinCount + 1
    elif playerChoice == 1 and computerChoice == 3:
        print("You throw rock, crushing the computer's scissors! You win!")
        playerWinCount = playerWinCount + 1
    elif playerChoice == 1 and computerChoice == 4:
        print("You throw rock, crushing the computer's lizard! You win!")
        playerWinCount = playerWinCount + 1
    elif playerChoice == 1 and computerChoice == 5:
        print("The computer throws Spock, vaporizing your rock! You lose!")
        computerWinCount = computerWinCount + 1

    # Paper conditions
    elif playerChoice == 2 and computerChoice == 1:
        print("You throw paper, covering the computer's rock! You win!")
        playerWinCount = playerWinCount + 1
    elif playerChoice == 2 and computerChoice == 3:
        print("The computer throws scissors, cutting your paper! You lose!")
        computerWinCount = computerWinCount + 1
    elif playerChoice == 2 and computerChoice == 4:
        print("The computer throws lizard, eating your paper! You lose!")
        computerWinCount = computerWinCount + 1
    elif playerChoice == 2 and computerChoice == 5:
        print("You throw paper, disproving the computer's Spock! You win!")
        playerWinCount = playerWinCount + 1

    # Scissors conditions
    elif playerChoice == 3 and computerChoice == 1:
        print("The computer throws rock, crushing your scissors! You lose!")
        computerWinCount = computerWinCount + 1
    elif playerChoice == 3 and computerChoice == 2:
        print("You throw scissors, cutting the computer's paper! You win!")
        playerWinCount = playerWinCount + 1
    elif playerChoice == 3 and computerChoice == 4:
        print("You throw scissors, decapitating the computer's lizard! You win!")
        playerWinCount = playerWinCount + 1
    elif playerChoice == 3 and computerChoice == 5:
        print("The computer throws Spock, smashing your scissors! You lose!")
        computerWinCount = computerWinCount + 1

    # Lizard conditions
    elif playerChoice == 4 and computerChoice == 1:
        print("The computer throws rock, crushing your lizard! You lose!")
        computerWinCount = computerWinCount + 1
    elif playerChoice == 4 and computerChoice == 2:
        print("You throw lizard, eating the computer's paper! You win!")
        playerWinCount = playerWinCount + 1
    elif playerChoice == 4 and computerChoice == 3:
        print("The computer throws scissors, decapitating your lizard! You lose!")
        computerWinCount = computerWinCount + 1
    elif playerChoice == 4 and computerChoice == 5:
        print("You throw lizard, poisoning the computer's Spock! You win!")
        playerWinCount = playerWinCount + 1

    # Spock conditions
    elif playerChoice == 5 and computerChoice == 1:
        print("You throw Spock, vaporizing the computer's rock! You win!")
        playerWinCount = playerWinCount + 1
    elif playerChoice == 5 and computerChoice == 2:
        print("The computer throws paper, disproving your Spock! You lose!")
        computerWinCount = computerWinCount + 1
    elif playerChoice == 5 and computerChoice == 3:
        print("You throw Spock, smashing the computer's scissors! You win!")
        playerWinCount = playerWinCount + 1
    elif playerChoice == 5 and computerChoice == 4:
        print("The computer throws a lizard, poisoning your Spock! You lose!")
        computerWinCount = computerWinCount + 1

    # Error handling
    else:
        print("Something went wrong, but I don't know what; how's that for error handling?")

    print("\nSCORES")
    print("You: ", playerWinCount)
    print("Computer: ", computerWinCount, "\n")

    while True:
        playAgain = input("Would you like to play again? Enter yes or no: ")
        if playAgain == "yes":
            print("\n")
            break
        elif playAgain == "no":
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid selection! Try again.")