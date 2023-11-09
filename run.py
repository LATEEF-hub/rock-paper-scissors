
import time
import pyfiglet
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
    print(Fore.BLUE + "HOW TO PLAY THE AMAZING ANIMAL QUIZ\033[39m")
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
    clear()
    input(Fore.BLUE + "Press Enter to continue...\033[39m")


def welcome():
    """
    Function to display welcome message and Game options for player.
    """

    while True:
        sleep(1)
        print_logo()
        sleep(1)
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
           break

        else:
          print(Fore.RED + "ERROR!\033[39m Invalid option please "
              "select 1, 2 or 3\n ")
          clear()    
          input(Fore.BLUE + "Press Enter to continue...\033[39m")
        # welcome()


def player_selection():
    """
    Function to get user's selection from keyboard.
    """
    user_input = input("Enter a choice (rock[1], paper[2], scissors[3]): ")
    selection = int(user_input)
    action = RPS(selection)
    return action



def start_game():
    """
    Starts a new game by calling functions to get user choices and compare them with computer choices.
    """




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
