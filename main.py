# Main Minesweeper program
from tkinter import *
import random

root = Tk()
root.title("Minesweeper")
root.geometry("500x500")

grid_dimensions = 3

num_squares = grid_dimensions**2
squares = []
mines = num_squares // 8
for mine in range(mines):
    squares.append("x")
while len(squares) < num_squares:
    squares.append("-")

random.shuffle(squares)
print(squares)

x = 0
y = 0
current_square = 0
for i in range(grid_dimensions):
    for j in range(grid_dimensions):
        btn = Button(root, width=3, text=squares[current_square])
        btn.grid(row=x, column=y)
        current_square += 1
        y += 1
    y = 0
    x += 1




root.mainloop()
