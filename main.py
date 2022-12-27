# Allows styling of the terminal
import curses
#initallizes curses module which takes over the terminal
# and helps runs different commands from it.
from curses import wrapper


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to Speed Tyoping Test!")
    stdscr.addstr("\nPress enter to begin!")
    stdscr.refresh()
    stdscr.getkey()

def main(stdscr):

    """
    STD screen aka standaard output which is the terminal
    since its where we're wiritng stuffy out to.
    - std.scr.clear() clears the entire screen
    - stdscr.addstr adds the string printed out to the console.
    - stdscr.refresh() once you start typing need to refresh the screen.
    - getkey() Waits for the user to type something so it doesn't immediealty close the program
    right away. User types and then it finishes.
    """
    #pairing of a foreground color an a background color.
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    start_screen(stdscr)

#Calls function
wrapper(main)