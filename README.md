# Battleship Game

[![Validated by PEP 8](https://img.shields.io/badge/PEP%208-validated-brightgreen.svg)](https://flake8.pycqa.org/)

This is a simple Battleship game implemented in Python, where the player tries to sink the computer's ships by guessing their locations on a grid.

## Instructions

1. Run the `run.py` file in your Python environment.
2. Enter the grid size and the number of ships when prompted.
3. Guess the row and column numbers to make a guess.
4. Keep guessing until you sink all the computer's ships or type 'quit' to exit the game.

## Usage

```bash
python run.py
```

## Sample Gameplay

```
Welcome to Battleship!
Try to sink the computer's ships.
Enter row and column numbers to make a guess.
Type 'quit' to exit the game.
  1 2 3 4 5
1 - - - - -
2 - - - - -
3 - - - - -
4 - - - - -
5 - - - - -
Enter your guess (row column): 3 3
You missed!
  1 2 3 4 5
1 - - - - -
2 - - - - -
3 - - M - -
4 - - - - -
5 - - - - -
Enter your guess (row column): 1 1
Congratulations! You sank a battleship!
  1 2 3 4 5
1 H - - - -
2 - - - - -
3 - - M - -
4 - - - - -
5 - - - - -
Congratulations! You won!
Do you want to play again? (yes/no): no
Exiting the game...
```

## Testing

1. **Test 1: Valid Guess**

   - Input: 3 3
   - Expected Output: "You missed!"

2. **Test 2: Invalid Guess**

   - Input: 6 6
   - Expected Output: "Your guess is off-grid. Try again."

3. **Test 3: Duplicate Guess**
   - Input: 1 1, 1 1
   - Expected Output: "You have already guessed that space. Try again."

## Known Bugs

- Sometimes the program may display the message "Your guess is off-grid." even for valid guesses. This occurs due to a rounding error

## Credits

- **ChatGPT**: Provided assistance in generating and refining the code.
- **Code Institute**: Contributed to the educational resources used for learning.
- **Mate Racz**: Assisted in code debugging and optimization.
- **WebDev**: Provided information and tutorials
- **YouTube**: Various tutorials and guides utilized for learning and inspiration.
- **Co-Pilot**: AI pair programmer developed by GitHub, provided code suggestions and enhancements.

## Libraries or Packages Used

- **Flake8**: Used for code linting and style checking to ensure adherence to PEP 8 guidelines.
- **Python 3.x**: The programming language used to develop the application.

### Imports

```python
import random
```
