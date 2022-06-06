# Main Minesweeper program
from tkinter import *
import tkinter.messagebox
import random

root = Tk()
root.title("Minesweeper")
root.geometry("500x500")


def check_for_mines(grid):
    """Looks for mines (marked as "x") and ups the value of any non-mine spaces adjacent to them by +1."""
    # ----------------------------------------------------------------------
    # CHECK FOR MINES
    # ----------------------------------------------------------------------
    for row_num in range(len(grid)):
        for col_index in range(len(grid)):
            if grid[row_num][col_index] == "x":

                # ----------------------------------------------------------------------
                # VERTICAL CHECKS
                # ----------------------------------------------------------------------
                # if a mine is found on the first row
                if row_num == 0:
                    # If it's the top row, it's the first row.
                    # No need to check for an earlier row_num
                    # +-------+  <- avoid checking this row
                    # + x 1 0 +
                    # + 1 0 0 +
                    # + 0 0 0 +
                    # +-------+
                    # checks directly below mine.
                    if grid[row_num + 1][col_index] != "x":
                        grid[row_num + 1][col_index] += 1

                    # checks down and to the right if the mine is the first item of the row
                    if col_index == 0 and grid[row_num + 1][col_index + 1] != "x":
                        grid[row_num + 1][col_index + 1] += 1
                    # checks down and to the left if the mine is the last item of the row
                    elif col_index == len(grid[row_num]) - 1 and grid[row_num + 1][col_index - 1] != "x":
                        grid[row_num + 1][col_index - 1] += 1
                    # checks all other diagonal spots that are the next row down
                    else:
                        try:
                            if grid[row_num + 1][col_index + 1] != "x":
                                grid[row_num + 1][col_index + 1] += 1
                        except IndexError:
                            print("outside the bounds of the grid")
                        finally:
                            pass
                        if grid[row_num + 1][col_index - 1] != "x":
                            grid[row_num + 1][col_index - 1] += 1

                # If a mine has been found on the last (bottom) row
                elif row_num == len(grid) - 1:
                    # If it's the bottom row, it's the last row.
                    # No need to check for a later row_num
                    # +-------+
                    # + 0 0 0 +
                    # + 1 0 0 +
                    # + x 1 0 +
                    # +-------+  <- avoid checking this row
                    # checks directly above the mine
                    if grid[row_num - 1][col_index] != "x":
                        grid[row_num - 1][col_index] += 1

                    # checks up and to the right if the mine is the first item of the row
                    if col_index == 0 and grid[row_num - 1][col_index + 1] != "x":
                        grid[row_num - 1][col_index + 1] += 1
                    # checks up and to the left if the mine is the last item of the row
                    elif col_index == len(grid[row_num]) - 1 and grid[row_num - 1][col_index - 1] != "x":
                        grid[row_num - 1][col_index - 1] += 1
                    # checks all other diagonal spots that are the next row up
                    else:
                        try:
                            if grid[row_num - 1][col_index + 1] != "x":
                                grid[row_num - 1][col_index + 1] += 1
                        except IndexError:
                            print("outside the bounds of the grid")
                        finally:
                            pass
                        if grid[row_num - 1][col_index - 1] != "x":
                            grid[row_num - 1][col_index - 1] += 1

                # if a mine is found on any other row
                else:
                    # checks directly below mine.
                    if grid[row_num + 1][col_index] != "x":
                        grid[row_num + 1][col_index] += 1
                    # checks directly above mine.
                    if grid[row_num - 1][col_index] != "x":
                        grid[row_num - 1][col_index] += 1

                    # checks diagonal spaces below mine
                    if col_index == 0 and grid[row_num + 1][col_index + 1] != "x":
                        grid[row_num + 1][col_index + 1] += 1
                    elif col_index == len(grid[row_num]) - 1 and grid[row_num + 1][col_index - 1] != "x":
                        grid[row_num + 1][col_index - 1] += 1
                    else:
                        try:
                            if grid[row_num + 1][col_index + 1] != "x":
                                grid[row_num + 1][col_index + 1] += 1
                        except IndexError:
                            print("outside the bounds of the grid")
                        finally:
                            pass
                        if grid[row_num + 1][col_index - 1] != "x":
                            grid[row_num + 1][col_index - 1] += 1

                    # checks diagonal spaces above mine
                    if col_index == 0 and grid[row_num - 1][col_index + 1] != "x":
                        grid[row_num - 1][col_index + 1] += 1
                    elif col_index == len(grid[row_num]) - 1 and grid[row_num - 1][col_index - 1] != "x":
                        grid[row_num - 1][col_index - 1] += 1
                    else:
                        try:
                            if grid[row_num - 1][col_index + 1] != "x":
                                grid[row_num - 1][col_index + 1] += 1
                        except IndexError:
                            print("outside the bounds of the grid")
                        finally:
                            pass
                        if grid[row_num - 1][col_index - 1] != "x":
                            grid[row_num - 1][col_index - 1] += 1

                # ----------------------------------------------------------------------
                # HORIZONTAL CHECKS
                # ----------------------------------------------------------------------
                if col_index == 0:
                    if grid[row_num][col_index + 1] != "x":
                        grid[row_num][col_index + 1] += 1
                elif col_index == len(grid[row_num]) - 1:
                    if grid[row_num][col_index - 1] != "x":
                        grid[row_num][col_index - 1] += 1
                else:
                    if grid[row_num][col_index - 1] != "x":
                        grid[row_num][col_index - 1] += 1
                    if grid[row_num][col_index + 1] != "x":
                        grid[row_num][col_index + 1] += 1
    return grid


def create_values(dimensions, mines):
    """Creates the values that will be placed and hidden in the minefield."""
    num_spaces = dimensions ** 2
    values = []
    for mine in range(mines):
        values.append("x")
    while len(values) < num_spaces:
        values.append(0)
    # shuffle and return the list to the main program
    random.shuffle(values)

    minefield_values = []
    for minefield_list_num in range(dimensions):
        # minefield
        globals()[f"minefield_grid_line{minefield_list_num}"] = []
        minefield_values.append(globals()[f"minefield_grid_line{minefield_list_num}"])

        for minefield_list_index in range(dimensions):
            # minefield
            x = values.pop()
            globals()[f"minefield_grid_line{minefield_list_num}"].append(x)
    minefield_values = check_for_mines(minefield_values)
    return minefield_values


def create_buttons(dimensions):
    buttons = []
    for btn_list_num in range(dimensions):
        # button field
        globals()[f"button_grid_line{btn_list_num}"] = []
        buttons.append(globals()[f"button_grid_line{btn_list_num}"])
        for btn_list_index in range(dimensions):
            # current_square = " "
            btn = Button(root, width=3, text=" ",
                         command=lambda row=btn_list_num, column=btn_list_index: reveal_space(row, column))
            btn.grid(row=btn_list_num, column=btn_list_index)
            globals()[f"button_grid_line{btn_list_num}"].append(btn)
    return buttons


def reveal_space(row, column):
    """Reveal the hidden value of the space. Ends the game and reveals the field if a mine has been found"""
    global button_field
    global minefield
    global continue_game
    global points
    global win_condition
    colors = ['blue', 'green', 'red', 'blue4', 'chocolate4', 'cyan3', 'black', 'gray']
    reveal = minefield[row][column]
    if reveal == "x" and continue_game:
        button_field[row][column].config(bg="red")
        continue_game = False
        reveal_all(len(minefield))
    elif reveal == "x":
        button_field[row][column].config(bg="red")
    else:
        button_field[row][column].config(fg=colors[reveal])
        points += 1
        if points == win_condition:
            continue_game = False
            reveal_all(len(minefield))
            tkinter.messagebox.showinfo("You Win!!", "You Win!")
    button_field[row][column].config(text=str(reveal))


def reveal_all(dimensions):
    """Reveals the values for the entire field."""
    for row in range(dimensions):
        for column in range(dimensions):
            reveal_space(row, column)



continue_game = True
points = 0
grid_dimensions = 7
total_spaces = grid_dimensions ** 2
num_mines = total_spaces // 8
win_condition = total_spaces - num_mines
minefield = create_values(grid_dimensions, num_mines)
# button_field is the actual grid of buttons that the values will be hidden behind
button_field = create_buttons(grid_dimensions)
# reveal_all(grid_dimensions)
print(minefield)
# print(button_field)
root.mainloop()
