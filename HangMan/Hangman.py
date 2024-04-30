
#Hangman

import random
from words import words
from hangman_visual import visual_dict
import string


def get_valid_word(words, min_length, max_length):
    word = random.choice(words)  # randomly chooses something from the list
    while len(word) < min_length or len(word) > max_length or "-" in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman_game(difficulty):
    #Defining difficulty levels
    difficulty_levels = {
        "easy": {"word_length": (3, 6), "lives": 5},
        "medium": {"word_length": (5, 8), "lives": 8},
        "difficult": {"word_length": (7, 10), "lives": 10}
    }
    #select word based on difficulty level

    min_length, max_length = difficulty_levels[difficulty]["word_length"]
    word = get_valid_word(words, min_length, max_length)

    #set lives based on difficulty level
    lives = difficulty_levels[difficulty]["lives"]

    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(visual_dict[lives]) #implementing hangman visual effects to show lives left
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


if __name__ == '__main__':
    difficulty = input("Choose difficulty (easy/medium/difficult): ").lower()
    hangman_game(difficulty)
