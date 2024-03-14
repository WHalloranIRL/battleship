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


# Function to randomly place ships on the grid
def place_ships(grid, num_ships):
    size = len(grid)
    for _ in range(num_ships):
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        
        # Ensure ships are not placed on top of each other
        while grid[x][y] == 'X':
            x = random.randint(0, size - 1)
            y = random.randint(0, size - 1)
        grid[x][y] = 'X'