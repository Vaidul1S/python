import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "O", " ", " ", " ", "#", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", " ", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#", "#", "#", " ", "#", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", " ", "#", " ", "#", " ", "#"],
    ["#", "#", "#", " ", "#", "#", "#", "#", "#", " ", "#", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", "#", " ", "#", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#", " ", "#", "#", " ", "#", "#", "#", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", "#"],
    ["#", "#", "#", " ", "#", " ", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", " ", "#", "X", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

def print_maze(maze, stdscr, path=[]):
    GREEN = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            stdscr.addstr(i, j*2, value, GREEN)

def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j

def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()
    


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)

    stdscr.clear()
    print_maze(maze, stdscr)
    # stdscr.addstr('Welcome to Maze Game!', curses.color_pair(3))
    # stdscr.addstr('\nPress any key to begin!', curses.color_pair(3))
    stdscr.refresh()
    stdscr.getkey()

wrapper(main) 