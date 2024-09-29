"""Structured Wordle!"""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(searched_str: str, searching_letter: str) -> bool:
    """Checks if the searching_letter is in the searched_str."""
    return searching_letter in searched_str


def emojified(guess_word: str, secret_word: str) -> str:
    """Generates emoji string for guess_word based on comparison with secret_word."""
    assert len(guess_word) == len(secret_word)
    emoji_str: str = ""
    secret_word_temp = list(secret_word)  
    guessed_correctly = [False] * len(secret_word)  

    for i in range(len(guess_word)):
        if guess_word[i] == secret_word[i]:
            emoji_str += GREEN_BOX
            guessed_correctly[i] = True  
            secret_word_temp[i] = None  
        else:
            emoji_str += WHITE_BOX  

    for i in range(len(guess_word)):
        if guess_word[i] != secret_word[i]:  
            if guess_word[i] in secret_word_temp:
                emoji_str = emoji_str[:i] + YELLOW_BOX + emoji_str[i+1:]
                secret_word_temp[secret_word_temp.index(guess_word[i])] = None

    return emoji_str


def input_guess(guess_length: int) -> str:
    """Prompts user for a guess of the required length."""
    user_word = input(f"Enter a {guess_length}-character word: ").lower()
    
    while len(user_word) != guess_length or not user_word.isalpha():
        user_word = input(f"Invalid input. Please enter a {guess_length}-character word using only letters: ").lower()
    
    return user_word


def main() -> None:
    """Main game loop for Wordle."""
    secret_word: str = "codes"  
    USER_TURNS: int = 6
    current_turn: int = 1
    answer: bool = False

    while current_turn <= USER_TURNS and not answer:
        print(f"=== Turn {current_turn}/{USER_TURNS} ===")
        user_guess: str = input_guess(len(secret_word))
        result = emojified(user_guess, secret_word)
        print(result)

        if user_guess == secret_word:
            answer = True
        else:
            current_turn += 1

    if answer:
        print(f"You won in {current_turn}/{USER_TURNS} turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
