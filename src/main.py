from graphics import Window
from maze import Maze
import sys


def main():
    
    print("Please enter specifications for your maze.")
    try:
        num_rows = int(float(input("Number of rows:")))
        num_cols = int(float(input("Number of columns:")))
        margin = int(float(input("Margin size between the maze and the window:")))
        screen_x = int(float(input("Screen-size in x-direction:")))
        screen_y = int(float(input("Screen-size in y-direction:")))
    except:
        print("Please enter a whole number and not a letter/symbol!")
        return

    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    print("maze created")
    is_solveable = maze.solve()
    if not is_solveable:
        print("maze can not be solved!")
    else:
        print("maze solved!")
    win.wait_for_close()


main()
