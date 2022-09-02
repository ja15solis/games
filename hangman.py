#Import packages
import random 
from list_words import words
import string

#Create functions to get the words without spaces and dashes
def get_valid_word (words):
    word = random.choice (words)
    while "-" in word or " " in word:
        word = random.choice (word)
    return word.upper()

def hangman():
    word = get_valid_word(words) 
    word_letters = set(word)    #letters in the word
    alphabet = set(string.ascii_uppercase)   #alphabet
    used_letters = set()      #set of letters selected by the user

    #lives
    lives = 6
    #get the user input
    while len(word_letters) > 0 and lives != 0:
        #letter used
        # ' '.join(['a', 'b', 'cd']) ---> ' a b cd'
        print(f'\nYou have {lives} left, lives You have used: ' , ' '.join(used_letters))

        #word with dashes, showing only the letters guessed correctly
        word_list= (letter if letter in used_letters else "-" for letter in word)
        print('Current Word: ', ' '.join(word_list))

        user_input = input('Guess a letter: ').upper()
        if user_input in alphabet - used_letters:
            used_letters.add(user_input) 
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives = lives - 1 #live taken away because of the wrong choise of the letter
                print('Letter not in Word.')
        elif user_input in used_letters:
            print("You have already used that letter. Please try again.")
        else:
            print("You have not selected a valid character. Please try again")
    if lives == 0:
        print(f'Sorry you have run out of lives. The Word was {word}\n')
    else:
        print(f'Yay! you have guessed the word "{word}" correctly with {lives} left. :)\n')