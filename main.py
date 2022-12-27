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

def wpm_test(stdscr):
    target_text = "Hello world lets type some text! Thye cow says moo."
    current_text = []

    stdscr.getkey()

    # Waits for user to type something then it append to the current text.
    while True:
        stdscr.clear()
        stdscr.addstr(target_text)

        # Then loop through every character/ keys in a for loop the user types by storing it in a list.
        # Then display the charater on the screen 
        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))

        stdscr.refresh()

        key = stdscr.getkey()

        # In ASCII 27 is the number for escape
        if ord(key) == 27:
            break

        current_text.append(key)


        # Helps clear the screen because if it doesn't it will repeat the text a ton of times.
        # Not clearing what the previous text says.
        stdscr.clear()
        stdscr.addstr(target_text)
        

def main(stdscr):

    """
    STD screen aka standaard output which is the terminal
    since its where we're writing stuff out to.
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
    wpm_test(stdscr)

#Calls function
wrapper(main)