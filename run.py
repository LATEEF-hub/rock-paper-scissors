import time
import pyfiglet
import pprint
import os
from time import sleep
import heading_art

from colorama import init, Fore, Back, Style


def rules():
    """
    This function displays the game's rules.
    """
    print(heading_art.logo)
    print(f'\033[2J')
    line_break()
    print(Fore.BLUE + "HOW TO PLAY THE AMAZING RPS GAME\033[39m")



def line_break():
    """
    # To make code less cluttered going forward
    """
    print("=========================================================")


def clear():
    """
    Clear the screen
    """

    os.system('clear')
    sleep(5)


def print_logo():
    """
    To print logo
    """
    print(heading_art.logo)


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


def main():
    welcome()


main()


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
