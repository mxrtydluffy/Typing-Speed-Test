# Allows styling of the terminal
import curses
# Initallizes curses module which takes over the terminal
# and helps runs different commands from it.
from curses import wrapper


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!\n")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):

    """
    #30-37
    Then loop through every character/keys in a for loop the user types 
    by storing it in a list. Then display the charater on the screen.
    Enumerate gets current text as well as the index in the list.
    "i" is equal to 0, 0 is going to reference beginning of list 
    and char is going to reference the first letter. In addition
    the character the user is on, like 1, 2 or 3, (index on the list)
    we must determine where the character should be placed.
    Here "i" will get incremented by 1.
    """

    stdscr.addstr(target)

    for i, char in enumerate(current):
        # Check for correct letters being typed
        correct_char = target[i]
        color = curses.color_pair(2)
        if char != correct_char:
            color = curses.color_pair(3)

        stdscr.addstr(0, i, char, color)

def wpm_test(stdscr):
    target_text = "Hello world lets type some text! The cow says moo."
    current_text = []

    # Waits for user to type something then it append to the current text.
    while True:
        # Helps clear the screen because if it doesn't it will repeat the text a ton of times.
        # Not clearing what the previous text says.
        stdscr.clear()
        display_text(stdscr, target_text, current_text)
        stdscr.refresh()

        key = stdscr.getkey()

        # In ASCII/unicode representation  27 is the number for escape
        if ord(key) == 27:
            break

        # Backspace on different operating systems can be represented in different characters.
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                # Since current text is keeping track of all the keys being typed.
                # We want to get rid of the last text being input.
                current_text.pop()
        else:
            current_text.append(key)
        

def main(stdscr):

    """
    STD screen aka standard output which is the terminal
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
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    
    start_screen(stdscr)
    wpm_test(stdscr)

#Calls function
wrapper(main)