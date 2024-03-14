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
        row_str = ""
        for cell in row:
            if cell == 'H' or cell == 'M':
                row_str += cell + " "
            else:
                row_str += "O "
        print(row_str)


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


# Function to check if a guess is valid and inside the grid boundries
def is_valid_guess(guess, size):
    x, y = guess
    return 0 <= x < size and 0 <= y < size

# Function to play the game
def play_game(size, num_ships):
    print("Welcome to Battleship!")
    print("Try to sink the computer's ships.")
    print("Enter row and column numbers to make a guess.")
    print("Type 'quit' to exit the game.")

    grid = create_grid(size)
    place_ships(grid, num_ships)
    print_grid(grid)

    while True:
        guess_str = input("Enter your guess (row column): ")
        if guess_str.lower() == 'quit':
            print("Exiting the game...")
            return
        try:
            guess = tuple(map(int, guess_str.split()))
            if not is_valid_guess(guess, size):
                print("Your guess is off-grid. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter row and column numbers.")
            continue

        x, y = guess
        if grid[x][y] == 'X':
            print("Congratulations! You sank a battleship!")
            grid[x][y] = '!'
            print_grid(grid)
            if all('X' not in row for row in grid):
                print("Congratulations! You won!")
                break
        else:
            print("You missed!")
            grid[x][y] = '-'
            print_grid(grid)



def main():
    while True:
        size = int(input("Enter the grid size: "))
        num_ships = int(input("Enter the number of ships: "))
        play_game(size, num_ships)
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Exiting the game...")
            break

if __name__ == "__main__":
    main()