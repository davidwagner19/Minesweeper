# Main Minesweeper program
from tkinter import *
import random

root = Tk()
root.title("Minesweeper")
root.geometry("500x500")


def create_space_values(dimensions):
    """Creates the values that will be placed and hidden in the minefield."""
    num_spaces = dimensions ** 2
    values = []
    mines = num_spaces // 8
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
    return minefield_values


grid_dimensions = 5
minefield = create_space_values(grid_dimensions)
print(minefield)


# ----------------------------------------------------------------------
# CHECK FOR MINES
# ----------------------------------------------------------------------
for list_num in range(grid_dimensions):
    for list_index in range(grid_dimensions):
        if minefield[list_num][list_index] == "x":

            # ----------------------------------------------------------------------
            # VERTICAL CHECKS
            # ----------------------------------------------------------------------
            # if a mine is found on the first row
            if list_num == 0:
                # If it's the top row, it's the first row.
                # No need to check for an earlier list_num
                # +-------+  <- avoid checking this row
                # + x 1 0 +
                # + 1 0 0 +
                # + 0 0 0 +
                # +-------+
                # checks directly below mine.
                if minefield[list_num + 1][list_index] != "x":
                    minefield[list_num + 1][list_index] += 1

                # checks down and to the right if the mine is the first item of the row
                if list_index == 0 and minefield[list_num + 1][list_index + 1] != "x":
                    minefield[list_num + 1][list_index + 1] += 1
                # checks down and to the left if the mine is the last item of the row
                elif list_index == len(minefield[list_num]) - 1 and minefield[list_num + 1][list_index - 1] != "x":
                    minefield[list_num + 1][list_index - 1] += 1
                # checks all other diagonal spots that are the next row down
                else:
                    try:
                        if minefield[list_num + 1][list_index + 1] != "x":
                            minefield[list_num + 1][list_index + 1] += 1
                    except IndexError:
                        print("outside the bounds of the grid")
                    finally:
                        pass
                    if minefield[list_num + 1][list_index - 1] != "x":
                        minefield[list_num + 1][list_index - 1] += 1

            # If a mine has been found on the last (bottom) row
            elif list_num == len(minefield) - 1:
                # If it's the bottom row, it's the last row.
                # No need to check for a later list_num
                # +-------+
                # + 0 0 0 +
                # + 1 0 0 +
                # + x 1 0 +
                # +-------+  <- avoid checking this row
                # checks directly above the mine
                if minefield[list_num - 1][list_index] != "x":
                    minefield[list_num - 1][list_index] += 1

                # checks up and to the right if the mine is the first item of the row
                if list_index == 0 and minefield[list_num - 1][list_index + 1] != "x":
                    minefield[list_num - 1][list_index + 1] += 1
                # checks up and to the left if the mine is the last item of the row
                elif list_index == len(minefield[list_num]) - 1 and minefield[list_num - 1][list_index - 1] != "x":
                    minefield[list_num - 1][list_index - 1] += 1
                # checks all other diagonal spots that are the next row up
                else:
                    try:
                        if minefield[list_num - 1][list_index + 1] != "x":
                            minefield[list_num - 1][list_index + 1] += 1
                    except IndexError:
                        print("outside the bounds of the grid")
                    finally:
                        pass
                    if minefield[list_num - 1][list_index - 1] != "x":
                        minefield[list_num - 1][list_index - 1] += 1

            # if a mine is found on any other row
            else:
                # checks directly below mine.
                if minefield[list_num + 1][list_index] != "x":
                    minefield[list_num + 1][list_index] += 1
                # checks directly above mine.
                if minefield[list_num - 1][list_index] != "x":
                    minefield[list_num - 1][list_index] += 1

                # checks diagonal spaces below mine
                if list_index == 0 and minefield[list_num + 1][list_index + 1] != "x":
                    minefield[list_num + 1][list_index + 1] += 1
                elif list_index == len(minefield[list_num]) - 1 and minefield[list_num + 1][list_index - 1] != "x":
                    minefield[list_num + 1][list_index - 1] += 1
                else:
                    try:
                        if minefield[list_num + 1][list_index + 1] != "x":
                            minefield[list_num + 1][list_index + 1] += 1
                    except IndexError:
                        print("outside the bounds of the grid")
                    finally:
                        pass
                    if minefield[list_num + 1][list_index - 1] != "x":
                        minefield[list_num + 1][list_index - 1] += 1

                # checks diagonal spaces above mine
                if list_index == 0 and minefield[list_num - 1][list_index + 1] != "x":
                    minefield[list_num - 1][list_index + 1] += 1
                elif list_index == len(minefield[list_num]) - 1 and minefield[list_num - 1][list_index - 1] != "x":
                    minefield[list_num - 1][list_index - 1] += 1
                else:
                    try:
                        if minefield[list_num - 1][list_index + 1] != "x":
                            minefield[list_num - 1][list_index + 1] += 1
                    except IndexError:
                        print("outside the bounds of the grid")
                    finally:
                        pass
                    if minefield[list_num - 1][list_index - 1] != "x":
                        minefield[list_num - 1][list_index - 1] += 1

            # ----------------------------------------------------------------------
            # HORIZONTAL CHECKS
            # ----------------------------------------------------------------------
            if list_index == 0:
                if minefield[list_num][list_index + 1] != "x":
                    minefield[list_num][list_index + 1] += 1
            elif list_index == len(minefield[list_num]) - 1:
                if minefield[list_num][list_index - 1] != "x":
                    minefield[list_num][list_index - 1] += 1
            else:
                if minefield[list_num][list_index - 1] != "x":
                    minefield[list_num][list_index - 1] += 1
                if minefield[list_num][list_index + 1] != "x":
                    minefield[list_num][list_index + 1] += 1


def reveal(row, column):
    """Reveal the hidden value of the space."""
    global button_field
    global minefield
    button_field[row][column]["text"] = str(minefield[row][column])


button_field = []
for list_num in range(grid_dimensions):
    # button field
    globals()[f"button_grid_line{list_num}"] = []
    button_field.append(globals()[f"button_grid_line{list_num}"])
    for list_index in range(grid_dimensions):
        # current_square = " "
        btn = Button(root, width=3, text=" ", command=lambda row=list_num, column=list_index: reveal(row, column))
        btn.grid(row=list_num, column=list_index)
        globals()[f"button_grid_line{list_num}"].append(btn)


# print(button_field)
root.mainloop()
