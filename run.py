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
    print("   " + " ".join(str(i) for i in range(1, len(grid) + 1)))
    for i, row in enumerate(grid, start=1):
        print("{:2d} {}".format(i, " ".join(cell for cell in row)))

# Function to randomly place ships on the grid
def place_ships(grid, num_ships):
    size = len(grid)
    for _ in range(num_ships):
        x = random.randint(1, size)
        y = random.randint(1, size)
        # Ensure ships are not placed on top of each other
        while grid[x - 1][y - 1] == 'X':
            x = random.randint(1, size)
            y = random.randint(1, size)
        grid[x - 1][y - 1] = 'X'

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
        size = int(input("Enter the grid size: "))
        num_ships = int(input("Enter the number of ships: "))
        play_game(size, num_ships)
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Exiting the game...")
            break

if __name__ == "__main__":
    main()
