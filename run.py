import pyfiglet
import pprint


def start_message():

    ascii = "ROCK\nPAPER\nSCISSORS\nLIZARD SPOCK"
    ascii_art = pyfiglet.figlet_format(ascii.ljust(10, ".").rjust(12, "+"))
    print(ascii_art)
    
start_message()