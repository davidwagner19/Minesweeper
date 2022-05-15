# Main Minesweeper program
from tkinter import *
import random

root = Tk()
root.title("Minesweeper")
root.geometry("500x500")

grid_dimensions = 4

num_squares = grid_dimensions**2
squares = []
mines = num_squares // 8
mines = 3
for mine in range(mines):
    squares.append("x")
while len(squares) < num_squares:
    squares.append(0)

random.shuffle(squares)
# print(squares)

minefield = []
for list_number in range(grid_dimensions):
    globals()[f"grid_line{list_number}"] = []
    minefield.append(globals()[f"grid_line{list_number}"])
    for square in range(grid_dimensions):
        x = squares.pop()
        globals()[f"grid_line{list_number}"].append(x)


print(minefield)

# Assign numbers to the squares adjacent to mines
# for square in range(len(squares)):
#     if squares[square] == "x":
#         if squares[square - grid_dimensions] != "x":
#             squares[square - grid_dimensions] = str(int(squares[square - grid_dimensions]) + 1)
#             print(squares[square - grid_dimensions])

for list_num in range(grid_dimensions):
    for list_index in range(grid_dimensions):
        if minefield[list_num][list_index] == "x":
            mine = minefield[list_num][list_index]
            if list_num == 0:
                # If it's the top row, it's the first row.
                # No need to check for an earlier list_num
                # +-------+  <- avoid checking this row
                # + x 1 0 +
                # + 1 0 0 +
                # + 0 0 0 +
                # +-------+
                if minefield[list_num + 1][list_index] != "x":
                    minefield[list_num + 1][list_index] += 1
            elif list_num == len(minefield) - 1:
                # If it's the bottom row, it's the last row.
                # No need to check for a later list_num
                # +-------+
                # + 0 0 0 +
                # + 1 0 0 +
                # + x 1 0 +
                # +-------+  <- avoid checking this row
                if minefield[list_num - 1][list_index] != "x":
                    minefield[list_num - 1][list_index] += 1
            else:
                if minefield[list_num - 1][list_index] != "x":
                    minefield[list_num - 1][list_index] += 1
                if minefield[list_num + 1][list_index] != "x":
                    minefield[list_num + 1][list_index] += 1

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


# x = 0
# y = 0
# current_square = 0
for i in range(grid_dimensions):
    for j in range(grid_dimensions):
        current_square = minefield[i][j]
        btn = Button(root, width=3, text=current_square)
        btn.grid(row=i, column=j)
    #     y += 1
    # y = 0
    # x += 1





root.mainloop()
