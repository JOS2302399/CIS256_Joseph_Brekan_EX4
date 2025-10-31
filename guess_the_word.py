import random

def word_guessing_game():
    word_list = ['sunflower', 'leather', 'monitor', 'tower', 'decoration', 'hunter']

    word_to_guess = random.choice(word_list)

    guessed_word = ["_"] * len(word_to_guess)

    attempts = 6

    guessed_letters = set()

    print('Welcome to the Word Guessing Game!')
    print('Can you guess the following word letter by letter?')
    print(' '.join(guessed_word))
    print(f'You have {attempts} incorrect attempts allowed.\n')

    while attempts > 0 and "_" in guessed_word:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print('Please enter a single alphabetic letter.\n')
            continue
        if guess in guessed_letters:
            print('You\'ve already guessed that letter. Try again.\n')
            continue
        
        guessed_letters.add(guess)

        if guess in word_to_guess:
            print('Good guess!\n')
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f'Wrong guess! Attempts left: {attempts}\n')

        print(' '.join(guessed_word))
        print()

    if '_' not in guessed_word:
        print(f'Congratulations! You guessed the word "{word_to_guess}" correctly!')
    else:
        print(f'Out of attempts! The word was "{word_to_guess}".')

if __name__ == '__main__':
    word_guessing_game()
    