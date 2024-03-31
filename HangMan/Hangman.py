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
    #setting the letters in the word
    word_letters = set(word)
    #in alphabetical order
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    #getting the user input
    while len(word_letters) > 0:
        #letter used
        #' '.join(['a', 'b', 'cd']) turns the string into ---> 'a b cd'
        print('You have used these letters: ', ' '.join(used_letters))
        #eliminating the used up letters and showcase the leftover letters to help
        #the user guess the next letter in that character/word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        #if it's a valid character that haven't used yet then add it into user_letter set
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
        #remove the letter from word letter if the letter is in the word is already guessed
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid character. Please try again.')
            #using loop to make the user guess the word until they have guessed the actual word

            #gets here when len(word_letter) > 0




user_input = input('Type something:')
#allow user to type in character that matches words from the list
print(user_input)

