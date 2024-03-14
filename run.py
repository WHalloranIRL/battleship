#importing the random number generator
import random

# Function to create a grid from user input
def create_grid(size):
    grid = []
    for _ in range(size):
        row = ['O'] * size
        grid.append(row)
    return grid

# Function to print the grid
def print_grid(grid):
    for row in grid:
        print(" ".join(row))