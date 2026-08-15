import random

WORDS = ["python", "hangman", "keyboard", "science", "puzzle"]
MAX_WRONG = 6

HANGMAN_PICS = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """,
]


def choose_word():
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_game():
    word = choose_word()
    guessed_letters = []
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print(f"Guess the word! You have {MAX_WRONG} incorrect guesses allowed.\n")

    while wrong_guesses < MAX_WRONG:
        print(HANGMAN_PICS[wrong_guesses])
        print("Word: " + display_word(word, guessed_letters))
        print(f"Wrong guesses left: {MAX_WRONG - wrong_guesses}")
        if guessed_letters:
            print("Guessed letters: " + ", ".join(sorted(guessed_letters)))

        guess = input("\nGuess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
            if all(letter in guessed_letters for letter in word):
                print(HANGMAN_PICS[wrong_guesses])
                print(f"Congratulations! You guessed the word: {word}")
                return
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")

    print(HANGMAN_PICS[wrong_guesses])
    print(f"Game over! You've used all {MAX_WRONG} incorrect guesses.")
    print(f"The word was: {word}")


def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing Hangman!")
            break


if __name__ == "__main__":
    main()
