# Allows styling of the terminal
import curses
#initallizes curses module which helps runs different commands from it.
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("Hello World I'm tynra code a speed test!!!")
    stdscr.refresh()
    # getkey() helps to not immediately close the program.
    stdscr.getkey()

#Calls function
wrapper(main)
