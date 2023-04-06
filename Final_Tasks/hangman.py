# Write a program that simulates a game of hangman.

import random

def play_hangman():
    words = ['python', 'java', 'javascript', 'ruby', 'php']
    word = random.choice(words)
    guesses = ''
    turns = 10
    
    while turns > 0:
        missed = 0
        for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
                missed += 1
        if missed == 0:
            print('\nCongratulations, you won!')
            return
        
        guess = input('\nGuess a letter: ').lower()
        guesses += guess
        
        if guess not in word:
            turns -= 1
            print(f'Wrong! You have {turns} more turns.')
            if turns == 0:
                print(f'Sorry, you lost. The word was {word}.')
