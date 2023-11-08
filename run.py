from ast import Compare
import time
import pyfiglet
import pprint
import random
import os
from time import sleep
import heading_art
from colorama import init, Fore, Back, Style


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

    sleep(3)
    clear()
    print(f'\033[2J')
    print(heading_art.logo)
    line_break()
    print(Fore.MAGENTA + "HOW TO PLAY THE AMAZING RPS GAME\033[39m")
    line_break()
    print("Lorem ipsimhhdbfb hidsb hd cbhd cbhs dchhd dh dhhds d dhhs d bshjjhd dhhs dfshb d . dhhs dhhsbbvf d")
    line_break()
    input(Fore.BLUE + "Press Enter to continue...\033[39m")


def welcome():
    """
    Function to display welcome message and Game options for player.
    """

    # clear()
    sleep(5)
    print_logo()
    sleep(5)
    print("Welcome to Rock, Paper, Scissors, Lizard, Spock Game\n\tYou have the following options:\n")
    print("\t1) Start Game\n\t2) Rules of the Game \n\t3) Exit Game")
    choice = int(
        input(Fore.BLUE + "Select your option between 1, 2 and 3:\n"))
    if choice == 1:
        print(Fore.GREEN+"Starting RPS Game...")
        sleep(2)
        start_game()
    elif choice == 2:
        print("Opening the Rules Book...")
        clear()
        rules()
    elif choice == 3:
        print(Fore.WHITE + "\nExiting The Game...")
        clear()
        print("Click on Run Program above to restart again!")

    else:
        print(Fore.RED + "ERROR!\033[39m Invalid option please "
              "select 1, 2 or 3\n ")
        input(Fore.BLUE + "Press Enter to continue...\033[39m")


def start_game():
    """
    Function that starts the actual game.
    """
    global score
    while True:
        computer_choice = random.randint(1, 6)
        human_choice = int(input(
            Fore.YELLOW + "Enter Your Choice (Rock=1,Paper=2,Scissors=3,Lizard=4,Spock=5):\033[39m"))
        result = Compare(computer_choice, human_choice)
        print(result)
        play_again = str(
            input(Fore.CYAN + "Do you want to play again? Y/N:\03[39m").lower())
        if play_again != 'y':
            break
        else:
            score = [0, 0]


def compare(comp, hum):
    """
    Compares the choices made by both player and computer.
    Returns a string with the outcome of the match.
    """
    comp_choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    human_choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    comp_name = comp_choices[comp - 1]
    human_name = human_choices[hum - 1]
    if comp > 3:
        comp_name = 'lizard'
    elif comp < 3:
        comp_name = 'spock'
    if hum > 3:
        human_name = 'lizard'
    elif hum < 3:
        human_name = 'spock'
    if comp == hum:
        return Fore.GREEN + f"\tIt is a tie! Both chose {human_name}."
    elif ((comp == 1 and hum in [2, 3]) or (comp == 2 and hum in [1, 3]) or (comp == 3 and hum in [1, 2])):
        score[0] += 1
        return Fore.GREEN + f"\tYou win! You chose {human_name}, I chose {comp_name}. \nYour current score is {score[0]} : {score[1]}"
    else:
        score[1] += 1
        return Fore.RED + f"\tI win! I chose {comp_name}, you chose {human_name}. \nMy current score is {score[0]} : {score[1]}"


def main():
    welcome()
    compare()
    start_game()


main()


# def welcome():
#     """
#     Display welcome message and game options
#     """
#     choice = ""

#     clear()
#     print_logo()
#     print("Welcome to Rock, Paper, Scissors, Lizard, Spock Game\n\tYou have the following options:\n")
#     print("\t1)Start Game")
#     print("\t2)Rules of the game")
#     print("\t3)Exit")
#     while True:
#             choice = int(input(Fore.BLUE + "Select your option between (1/2/3):"))
#             if choice == 1:
#                 print(Fore.GREEN + "Starting RPS Game...")
#             elif choice == 2:
#                 print(Fore.CYAN + "Opening RPS Rules...")
#                 sleep(5)
#                 rules()
#             elif choice == 3:
#                 print("Game Exited to restart the game, click on Run Program"
#                   " above")
#                 break
#             else:
#                 print(Fore.RED + "\nERROR!\033[39m Invalid option please "
#                   "select 1, 2, 3 or 4\n ")
#                 input(Fore.BLUE + "Press Enter to continue...\033[39m")


# def rules():
#     """


#     choice = input(Fore.BLUE + "Enter your choice : ").strip().lower()

#     if choice == "1":
#         print("Opening the rulebook...")
#         sleep(5)
#         rules()
#     else:
#         print(Fore.RED + "ERROR!\033[39m Invalid option please "
#               "select 1, 2, 3 or 4\n ")
#         input(Fore.BLUE + "Press Enter to continue...\033[39m")


# def play_again():
#     """
#     Play Again.
#     After completing a quiz or game the user is asked
#     do they want to play again.
#     If yes the user is brought back to the main function to pick what to play.
#     If no the terminal is closed.
#     """
#     play_again_input = input("Would you like to play another game?\nY/N\n").lower()
#     if play_again_input == "y":
#         sleep(1)
#         os.system('clear')
#         main()

#     elif play_again_input == “n”:
#         os.system('clear')
#         exit_terminal()

#     else:
#         print("Please choose Y or N")

# def exit_terminal():
