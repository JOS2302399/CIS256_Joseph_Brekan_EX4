# Joseph Brekan
# CIS256
# EX 4

import random

def word_guessing_game():
    # Predefined list of words
    word_list = ['sunflower', 'leather', 'monitor', 'tower', 'decoration', 'hunter']

    # Select a random word from the list
    word_to_guess = random.choice(word_list)

    # Create a display version of the word
    guessed_word = ["_"] * len(word_to_guess)

    # Set number of attempts
    attempts = 6

    # Score guessed letters to prevent repeats
    guessed_letters = set()

    print('Welcome to the Word Guessing Game!')
    print('Can you guess the following word letter by letter?')
    print(' '.join(guessed_word))
    print(f'You have {attempts} incorrect attempts allowed.\n')

    # Main game loop
    while attempts > 0 and "_" in guessed_word:
        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print('Please enter a single alphabetic letter.\n')
            continue
        if guess in guessed_letters:
            print('You\'ve already guessed that letter. Try again.\n')
            continue
        
        guessed_letters.add(guess)

        # Check if the guessed letter is in the word
        if guess in word_to_guess:
            print('Good guess!\n')
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f'Wrong guess! Attempts left: {attempts}\n')

        # Display current progress
        print(' '.join(guessed_word))
        print()

    # Check win/lose condition
    if '_' not in guessed_word:
        print(f'Congratulations! You guessed the word "{word_to_guess}" correctly!')
    else:
        print(f'Out of attempts! The word was "{word_to_guess}".')

# Run the game
if __name__ == '__main__':
    word_guessing_game()
