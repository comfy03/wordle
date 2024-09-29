# Structured Wordle

### Description

This is a simple terminal-based Wordle clone built in Python. The game is inspired by the popular word-guessing game, Wordle. The objective is to guess a secret 5-letter word within 6 attempts. After each guess, feedback is provided using colored emoji-like symbols:

🟩 (Green Box): The letter is in the correct position.<br>
🟨 (Yellow Box): The letter is in the word but in the wrong position.<br>
⬜ (White Box): The letter is not in the word.
Features

The game allows the user to input guesses and receive feedback on how close their guess is to the secret word.
The feedback adheres to the Wordle rules: exact matches are marked green, letters that exist in the word but are misplaced are marked yellow, and incorrect letters are marked with white boxes.
You have 6 turns to guess the secret word.

#### <u> How It Works <u/>

The user is prompted to input a 5-letter word.
The program compares the user's guess to the secret word.
Feedback is given using green, yellow, and white box symbols:
Green boxes for correct letters in the correct position.
Yellow boxes for correct letters in the wrong position.
White boxes for incorrect letters.
The user has up to 6 turns to guess the correct word. If they guess correctly before the turns run out, they win. Otherwise, they lose.
