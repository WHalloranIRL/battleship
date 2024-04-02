# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

# Function to create a grid of given size
def create_grid(size):
    grid = []
    for _ in range(size):
        row = [' '] * size  # Initialize with empty spaces
        grid.append(row)
    return grid

# Function to print the grid with hits and misses
def print_grid(grid):
    for i, row in enumerate(grid, start=1):
        printable_row = []
        for j, cell in enumerate(row, start=1):
            if cell == 'H' or cell == 'M':  # Show hits and misses
                printable_row.append(cell)
            else:
                printable_row.append('-')  # Hide ships and unguessed spaces
        print(f"{i} {' '.join(printable_row)}")

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

# Function to check if a guess is valid (within grid boundaries)
def is_valid_guess(guess, size):
    x, y = guess
    return 1 <= x <= size and 1 <= y <= size

# Function to play the game
def play_game(size, num_ships):
    print("Welcome to Battleship!")
    print("Try to sink the computer's ships.")
    print("Enter row and column numbers to make a guess.")
    print("Type 'quit' to exit the game.")

    grid = create_grid(size)
    place_ships(grid, num_ships)
    print_grid(grid)

    guessed_coordinates = set()  # Set to store guessed coordinates

    while True:
        guess_str = input("Enter your guess (row column): \n")
        if guess_str.lower() == 'quit':
            print("Exiting the game...")
            return
        try:
            guess = tuple(map(int, guess_str.split()))
            if not is_valid_guess(guess, size):
                print("Your guess is off-grid. Try again.")
                continue
            if guess in guessed_coordinates:
                print("You have already guessed that space. Try again.")
                continue
            guessed_coordinates.add(guess)
        except ValueError:
            print("Invalid input. Please enter row and column numbers.")
            continue

        x, y = guess
        if grid[x - 1][y - 1] == 'X':
            print("Congratulations! You sank a battleship!")
            grid[x - 1][y - 1] = 'H'  # Mark hit
            print_grid(grid)
            if all('X' not in row for row in grid):
                print("Congratulations! You won!")
                break
        else:
            print("You missed!")
            if grid[x - 1][y - 1] != 'M':  # Avoid marking multiple misses on the same spot
                grid[x - 1][y - 1] = 'M'  # Mark miss
            print_grid(grid)

# Main function
def main():
    while True:
        size = int(input("Enter the grid size: \n"))
        num_ships = int(input("Enter the number of ships: \n"))
        play_game(size, num_ships)
        play_again = input("Do you want to play again? (yes/no): \n")
        if play_again.lower() != 'yes':
            print("Exiting the game...")
            break

if __name__ == "__main__":
    main()