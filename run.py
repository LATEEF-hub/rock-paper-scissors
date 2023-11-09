import random
import os
from time import sleep
import heading_art
from colorama import init, Fore, Back, Style
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
 
victories = {
        RPS.ROCK: [RPS.SCISSORS],  # Rock beats scissors
        RPS.PAPER: [RPS.ROCK],  # Paper beats rock
        RPS.SCISSORS: [RPS.PAPER]  # Scissors beats paper
    }
   


def line_break():
    """
    # To make code less cluttered going forward
    """
    print("=========================================================")


def clear():
    """
    Clear the screen
    """
    sleep(4)
    os.system('clear')


def print_logo():
    """
    To print logo
    """
    print(heading_art.logo)


def rules():
    """
    This function displays the game's rules.
    """

    print(f'\033[2J')
    line_break()
    print(Fore.BLUE + "HOW TO PLAY THE AMAZING ROCK PAPER SCISSORS GAME\033[39m")
    line_break()
    print("Rock Paper Scissors (RPS) is a zero-sum game, typically played by two people using their hands and no tools.\n"
          "Players make hand shapes, each with a certain degree of power, ultimately leading to an outcome.\n")
    print("There are three options ROCK PAPER & SCISSORS\n")
    print("ROCK: The rock is when you place your hand into the form of a simple fist.\n")
    print("PAPER: The paper is when you place your hand in an outstretched position.\n")
    print("SCISSORS: This is when you hold your fist with your index and middle finger pointing outwards in a V shape.\n")
    line_break()
    print("Rock wins against scissors.\n"
          "Scissors win against paper.\n"
          "Paper wins against rock.\n")
    print("Select your answer by typing one of the options\n"
          "and pressing Enter afterwards.\n")
    line_break()
    input(Fore.BLUE + "Press Enter to continue...\033[39m")
    clear()

    


def welcome():
    """
    Function to display welcome message and Game options for player.
    """

    while True:
        sleep(1)
        print_logo()
        sleep(1)
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock Game\n\tYou have the following options:\n")
        print("\t1) Start Game\n\t2) Rules of the Game \n\t3) Exit Game\n")
        choice = int(
        input(Fore.BLUE + "Select your option between 1, 2 and 3:\n"))
        if choice == 1:
           print(Fore.GREEN+"\nStarting RPS Game...")
           sleep(2)
           clear()
           print(heading_art.logo+"\n")
           start_game()
        elif choice == 2:
           print("Opening the Rules Book...")
           clear()
           rules()
        elif choice == 3:
           print(Fore.WHITE + "\nExiting The Game...")
           clear()
           print("Click on Run Program above to restart again!")
           break

        else:
          print(Fore.RED + "ERROR!\033[39m Invalid option please "
              "select 1, 2 or 3\n ")  
          input(Fore.BLUE + "Press Enter to continue...\033[39m")
          clear()


def player_selection():
    """
    Function to get user's selection from keyboard.
    """
    choices = [f"{action.name}[{action.value}]" for action in RPS]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): \n"))
    action = RPS(selection)
    return action


def get_computer_selection():
    """
    Function to randomly select computer's move.
    """
    selection = random.randint(0, len(RPS) - 1)
    action = RPS(selection)
    return action    

def determine_winner(user_action, computer_action):
    defeats = victories[user_action] 
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie! 😜")
    elif computer_action in defeats:
        print(f"{user_action.name} beats {computer_action.name}! You win! 🎉")
    else:
        print(f"{computer_action.name} beats {user_action.name}! You lose. 😩")


def start_game():
    while True:
        try:
            user_choice = player_selection()
            computer_choice = get_computer_selection()
            print("")
            print("Player chose " + str(RPS(user_choice)).replace("RPS.", ""))
            print("")
            print("Computer chose " + str(RPS(computer_choice)).replace("RPS.", ""))
            print("")
            determine_winner(user_choice, computer_choice)
            play_again = input("\nDo you want to play again? y/n: ")
            if play_again.lower().startswith('y'):
                clear()
                main()
            else:
                print("\n")
                print("Thanks for playing!...\n")
                sleep(2)
                clear()
                main()
                
        except ValueError as e:
            print(e)
            continue        



def main():
    welcome()

main()


