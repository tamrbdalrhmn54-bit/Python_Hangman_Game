import random


HANGMAN_STAGES = [
    '''
  +---+
  |   |
      |
      |
      |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
'''
]


WORDS = [
    "python",
    "computer",
    "security",
    "network",
    "programming",
    "keyboard"
]


def choose_word():
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    result = ""

    for letter in word:
        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "

    return result


def get_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1:
            print("❌ Please enter ONE letter.")
            continue

        if not guess.isalpha():
            print("❌ Please enter a letter, not a number or symbol.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        return guess


def play_game():
    word = choose_word()

    guessed_letters = []
    lives = 6

    print("\n🎮 Welcome to Hangman!")
    print("Try to guess the word.")
    print(HANGMAN_STAGES[0])

    while lives > 0:

        print("\nWord:", display_word(word, guessed_letters))
        print("Guessed letters:", " ".join(guessed_letters))
        print("Lives:", lives)

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct!")

        else:
            lives -= 1
            print("❌ Wrong!")
            print(HANGMAN_STAGES[6 - lives])

        if all(letter in guessed_letters for letter in word):
            print("\n🎉 You Win!")
            print(f"The word was: {word}")
            return

    print("\n💀 You Lose!")
    print(f"The word was: {word}")


play_game()