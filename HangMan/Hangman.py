import random
import string

from words import words

def get_valid_word(words):
    word = random.choice(words) #assiging words into random choice to randomly choices word from list
    while '-' in word or ' ' in word:
        word = random.choice(words)

        return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    #getting the user input
    while len(word_letters) > 0:
        print('You have used these letters: ', ' '.join(used_letters))
    #eliminating the used up letters and showcase the leftover letters to help
    #the user guess the next letter in that character/word
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('Current word: ', ' '.join(word_list))

    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('You have already used that letter. Please try again.')
        else:
            print('Invalid letter. Please try again.')

            #using loop to make the user guess the word until they have guessed the actual word




user_input = input('Type something:') #allow user to type in character that matches words from the list
print(user_input)

