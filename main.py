# Main Minesweeper program
from tkinter import *
import random

root = Tk()
root.title("Minesweeper")
root.geometry("500x500")

grid_dimensions = 6

num_squares = grid_dimensions**2
squares = []
mines = num_squares // 8

for mine in range(mines):
    squares.append("x")
while len(squares) < num_squares:
    squares.append(0)

random.shuffle(squares)

minefield = []
for list_number in range(grid_dimensions):
    globals()[f"grid_line{list_number}"] = []
    minefield.append(globals()[f"grid_line{list_number}"])
    for square in range(grid_dimensions):
        x = squares.pop()
        globals()[f"grid_line{list_number}"].append(x)

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
                    if minefield[list_num + 1][list_index + 1] != "x":
                        minefield[list_num + 1][list_index + 1] += 1
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
                    if minefield[list_num - 1][list_index + 1] != "x":
                        minefield[list_num - 1][list_index + 1] += 1
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
                    if minefield[list_num + 1][list_index + 1] != "x":
                        minefield[list_num + 1][list_index + 1] += 1
                    if minefield[list_num + 1][list_index - 1] != "x":
                        minefield[list_num + 1][list_index - 1] += 1

                # checks diagonal spaces above mine
                if list_index == 0 and minefield[list_num - 1][list_index + 1] != "x":
                    minefield[list_num - 1][list_index + 1] += 1
                elif list_index == len(minefield[list_num]) - 1 and minefield[list_num - 1][list_index - 1] != "x":
                    minefield[list_num - 1][list_index - 1] += 1
                else:
                    if minefield[list_num - 1][list_index + 1] != "x":
                        minefield[list_num - 1][list_index + 1] += 1
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


for i in range(grid_dimensions):
    for j in range(grid_dimensions):
        current_square = minefield[i][j]
        btn = Button(root, width=3, text=current_square)
        btn.grid(row=i, column=j)

root.mainloop()
