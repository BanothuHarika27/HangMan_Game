# HangMan_Game

- This is a simple command-line implementation of the classic Hangman game in Python. The game randomly selects a word from a predefined list, and the player must guess the letters of the word within a limited number of incorrect guesses (lives). The game provides visual feedback through a series of hangman stages, which change as the player makes incorrect guesses.

## Features:
- Random Word Selection: The game randomly selects a word from a list of words stored in an external file.
* User Input: Players can input their guesses for letters in the word.
+ Dynamic Display: The current state of the word is displayed with underscores representing unguessed letters.
- Lives System: Players have a limited number of incorrect guesses (lives), and the game ends when they run out of lives or successfully guess the word.
- Visual Feedback: The game displays different stages of the hangman based on the number of incorrect guesses.
## How It Works
- Word Selection: The game starts by randomly selecting a word from a list of words defined in word_file_hangman.py.
- Display Initialization: The display is initialized with underscores representing each letter in the chosen word.
- Game Loop: The game enters a loop where it prompts the player to guess a letter:
   - If the guessed letter is in the word, it updates the display.
   - If the guessed letter is not in the word, it decreases the number of lives.
   - The game checks for win or lose conditions after each guess.
   - End of Game: The game ends when the player either successfully guesses the word or runs out of lives, displaying the appropriate message.
## Requirements:
 -  Python 3.x
 -  hangman_stages.py: A module containing the visual representation of the hangman stages.
 -  word_file_hangman.py: A module containing a list of words for the game.
