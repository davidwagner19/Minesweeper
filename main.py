# Main Minesweeper program
from tkinter import *
import random

root = Tk()
root.title("Minesweeper")
root.geometry("500x500")

grid_dimensions = 7

num_squares = grid_dimensions**2
squares = []
mines = num_squares // 8

for mine in range(mines):
    squares.append("x")
while len(squares) < num_squares:
    squares.append(0)

random.shuffle(squares)

reveal_field = []
minefield = []
# button_field = []
for list_num in range(grid_dimensions):
    # reveal field
    globals()[f"hidden_grid_line{list_num}"] = []
    reveal_field.append(globals()[f"hidden_grid_line{list_num}"])
    # minefield
    globals()[f"minefield_grid_line{list_num}"] = []
    minefield.append(globals()[f"minefield_grid_line{list_num}"])

    for list_index in range(grid_dimensions):
        # reveal field
        globals()[f"hidden_grid_line{list_num}"].append(False)
        # minefield
        x = squares.pop()
        globals()[f"minefield_grid_line{list_num}"].append(x)


print(minefield)

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

    # reveal_field[revealed_list_num][revealed_list_index] = True
    # btn["text"] = "Clicked"
    button_field[row][column]["text"] = str(minefield[row][column])


# TODO
# Need to find a way to re-reference the buttons after they've been placed onto the grid
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


print(button_field)
root.mainloop()
