# Python-hangman-game
The Hangman game is a classic word-guessing game implemented in Python. Players guess letters to uncover a hidden word while trying to avoid running out of lives. The game features ASCII art for the hangman and provides an engaging way to improve vocabulary.
# Hangman Game Logic Breakdown

## Step 1: Game Setup and Initialization

Before the game begins, all necessary components are prepared.

### 1.1 Import Modules
- Import the `random` module to allow the computer to pick a random word.

### 1.2 Define Game Assets
- **word_list**: Create a list of words from which the game will randomly choose.
- **stages**: Create a list of multi-line strings. Each string is an ASCII art depiction of a stage of the hangman. The list is ordered such that `stages[0]` is the final "game over" state, and `stages[6]` is the initial empty state.

### 1.3 Initialize Game State
- `lives = 6`: The player starts with 6 lives.
- `chosen_word = random.choice(word_list)`: A word is randomly selected from the `word_list` for the current game.
- `display = []`: An empty list is created to show the player's progress. It is filled with underscores (_), one for each letter in the `chosen_word`.
- `game_over = False`: A boolean flag is set to False to control the main game loop.

## Step 2: Start the Main Game Loop

The core of the game runs inside a while loop. The loop continues as long as the `game_over` flag is False. Each iteration of the loop represents one turn.

## Step 3: Handle User Input

Inside the loop, the game needs to get a guess from the user.

- Use `input()` to prompt the user to "Guess a letter".
- Convert the input to lowercase using `.lower()` to ensure the check is case-insensitive (e.g., 'A' is treated the same as 'a').

## Step 4: Check the Guessed Letter Against the Word

After getting the user's guess, the program checks if it's a correct letter.

- Loop through the `chosen_word` using an index (e.g., `for position in range(len(chosen_word))`).
- In each iteration, compare the letter at the current position in the `chosen_word` with the `guessed_letter`.
- If they match, replace the underscore in the `display` list at the same position with the `guessed_letter`.

## Step 5: Handle Incorrect Guesses and Update Lives

If the guess is wrong, the player must be penalized.

- After the loop in Step 4, check if the `guessed_letter` is not present in the `chosen_word`.
- If the guess was incorrect:
  - Decrement `lives` by 1.
  - Check if `lives` has reached 0. If it has, the player has lost. Set `game_over = True` and print a "You Lose" message.

## Step 6: Update the Display and Check for a Win

After every guess, the game state is updated and checked for a win condition.

- **Show Progress**: Print the `display` list to show the user which letters they have guessed correctly.
- **Show Hangman**: Print the hangman ASCII art from the `stages` list that corresponds to the current number of lives (e.g., `print(stages[lives])`).
- **Check for Win**: Check if the `display` list no longer contains any underscores (_).
  - If there are no underscores left, the user has successfully guessed the word. Set `game_over = True` and print a "You Win" message.

The loop continues until either the player runs out of lives (loss) or correctly guesses the entire word (win).
