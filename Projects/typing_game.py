import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 4, 'Welcome to Speed Typing Game!', curses.color_pair(1))
    stdscr.addstr(1, 4, '\nPress any key to begin!', curses.color_pair(1))
    stdscr.refresh()
    stdscr.getkey()

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)

    
    start_screen(stdscr)

wrapper(main)