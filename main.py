# Allows styling of the terminal
import curses
# Initializes curses module which takes over the terminal
# and helps runs different commands from it.
from curses import wrapper
import time


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!\n")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):

    """
    #30-37
    Loops through every character/keys in a for loop the user types 
    by storing it in a list. Then display the character on the screen.
    Enumerate gets current text as well as the index in the list.
    "i" is equal to 0, 0 is going to reference beginning of list 
    and "char" is going to reference the first letter. In addition
    the character the user is on, like 1, 2 or 3, (index on the list)
    we must determine where the character should be placed.
    Here "i" will get incremented by 1.
    """

    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        # Check for correct letters being typed
        correct_char = target[i]
        color = curses.color_pair(2)
        if char != correct_char:
            color = curses.color_pair(3)

        stdscr.addstr(0, i, char, color)

def wpm_test(stdscr):

    """
    #67
    Calculation to determing wpm.
    Number or words is calculated when the number of characters is divided by 5.
    Therefore, Number of Words = Total Keys Typed / 5
    WPM = Total Number of Words / Time Elasped in Minutes
    This calculation is rounded down
    """

    target_text = ("According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible. Yellow, black. Yellow, black. Yellow, black. Yellow, black. Ooh, black and yellow! Let's shake it up a little. Barry! Breakfast is ready! Coming! Hang on a second. Hello? Barry? Adam? Can you believe this is happening? I can't. I'll pick you up. Looking sharp. Use the stairs, Your father paid good money for those. Sorry. I'm excited.")
    current_text = []
    wpm = 0
    # Very large number | Stores epoch
    start_time = time.time()
    # Nodelay is basically telling to not delay by waiting for the user to press a key.
    stdscr.nodelay(True)

    # Waits for user to type something then it append to the current text.
    while True:
        # Time elapsed is going to be 0 sec since the time between we calculated this is going to be the exact same time.
        # If time.time() & start_time is 0 it will give the max of 1. This is implemented to not to divide 0 by 0
        time_elapsed = max(time.time() - start_time, 1)

        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        # Helps clear the screen because if it doesn't it will repeat the text a ton of times.
        # Not clearing what the previous text says.
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        # Check if user text is equal to whatever the target text is.
        # Can do this by converting list to string to check if it matches the targeted text.
        # Here it combines every single character form this list 
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            # Breaks outside of while loop
            break

        # "stdscr.getkey()" is a block meaning it does nothing unitl user types the key.
        # "try" allows to not let program crash. If it does "except" is executed and continue beings back at while loop.
        try:
            key = stdscr.getkey()
        except:
            continue

        # In ASCII/unicode representation  27 is the number for escape
        if ord(key) == 27:
            break

        # Backspace on different operating systems can be represented in different characters.
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                # Since current text is keeping track of all the keys being typed.
                # We want to get rid of the last text being input.
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)
        

def main(stdscr):

    """
    STD screen aka standard output which is the terminal
    since its where user is writing stuff out to.
    - std.scr.clear() clears the entire screen
    - stdscr.addstr adds the string printed out to the console.
    - stdscr.refresh() once you start typing need to refresh the screen.
    - getkey() Waits for the user to type something so it doesn't immediately close the program
    right away. User types and then it finishes.
    """

    #pairing of a foreground color an a background color.
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    
    start_screen(stdscr)
    while True:
        # Going to return function.
        wpm_test(stdscr)

        stdscr.addstr(2, 0, "You completed the Speed Writing Test! Press any key to to continue...")
        key = stdscr.getkey()

        if ord(key) == 27:
            break

wrapper(main)