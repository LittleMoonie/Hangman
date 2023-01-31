import os
import random
import time
import words
from wordhoard import Definitions

# Console Cleaner #
def clrscr():
  ''' Clears the console in order to make a more pleasant game '''
  if os.name == 'posix':  # compatible with Unix/Linux/MacOS/BSD/etc
    os.system('clear')
  elif os.name in ('nt', 'dos', 'ce'):  # compatible with DOS/Windows
    os.system('CLS')

    
# Global Declariong Section #
global typeSelector
global randomWord

# Gets the type of word you want to guess between Adjective | Noun | Verb #
def word_Type(type):

    match type:
        case "adjectives":
            randomWord = random.choice(words.adjective_Function())
            return randomWord
        case "nouns":
            randomWord = random.choice(words.nouns_Function())
            return randomWord
        case "verbs":
            randomWord = random.choice(words.verbs_Function())
            return randomWord

# Gets the word needing to be guessed funtion #
def wordFetcher():
    global count
    global display
    global guessing_word
    global already_guessed
    global length
    global start_game
    global original_word
    guessing_word = randomWord
    original_word = guessing_word
    length = len(guessing_word)
    count = 0
    display = '_' * length
    already_guessed = []
    start_game = ''

# Restarting the game after losing or winning function #
def restart_game():
    global start_game
    while True:
        start_game = input('Do you wish to play again? (Y/N)\n').casefold()
        if start_game == 'y' or start_game == 'ye' or start_game == 'yes':
            print('The game will now start. Get ready!')
            typeSelector = input('Please select the word type you would like to use between the following choices : "Adjectives", "Nouns", "Verbs".\n').casefold()
            word_Type(typeSelector)
            while True:
                if typeSelector == "adjectives" or typeSelector == "nouns" or typeSelector == "verbs":
                    print(f'You have chosen the word type : {typeSelector}. Goodluck!\n')
                    time.sleep(2)
                    clrscr()
                    wordFetcher()
                    hangman()

        elif start_game == 'n' or start_game == 'no':
            print('Thank you for playing. Hoping to see you soon!')
            time.sleep(2)
            clrscr()
            exit()

        else:
            print(f'You entered {start_game} which is not part of the given options. Please try again while providing a Y/N answer.')

# Hangman Game Function #
def hangman():
    global count
    global display
    global guessing_word
    global already_guessed
    global start_game
    global typeSelector

    limit = 5
    definition = Definitions(search_string=original_word)
    definition_results = definition.find_definitions()
    print(f'Here is a definition of the word you are trying to find: {definition_results}\n')
    print(f'You currently have {count}/5 lost tries done. Be careful!\n')
    guess = input(f'This is the word you need to find: {display}.\nEnter your guess here: \n').casefold()
    guess = guess.strip()
    
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= '9':
        print('Invalid Input, Try a letter!\n')
        hangman()

    elif guess in guessing_word:
        already_guessed.extend([guess])
        index = ( [pos for pos, char in enumerate(guessing_word) if char == guess])
        for index in index:
            guessing_word = guessing_word[:index] + '_' +guessing_word[index+1:]
            display = display[:index] + guess + display[index+1:]
        print(display + '\n')

    elif guess in already_guessed:
        print('Try another letter.\n')
        time.sleep(2)

    else:
        count += 1
        if count == 1:
            print('   _____ \n'
                  '  |      \n'
                  '  |      \n'
                  '  |      \n'
                  '  |      \n'
                  '  |      \n'
                  '  |      \n'
                  '__|__\n')
            print(f'Wrong guess. {limit - count} guesses remaining\n')
            time.sleep(2)
            clrscr()

        elif count == 2:
            print('   _____ \n'
                  '  |     |\n'
                  '  |     |\n'
                  '  |      \n'
                  '  |      \n'
                  '  |      \n'
                  '  |      \n'
                  '__|__\n')
            print(f'Wrong guess. {limit - count} guesses remaining\n')
            time.sleep(2)
            clrscr()

        elif count == 3:
           print('   _____ \n'
                 '  |     |\n'
                 '  |     |\n'
                 '  |     |\n'
                 '  |      \n'
                 '  |      \n'
                 '  |      \n'
                 '__|__\n')
           print(f'Wrong guess. {limit - count} guesses remaining\n')
           time.sleep(2)
           clrscr()

        elif count == 4:
            print('   _____ \n'
                  '  |     |\n'
                  '  |     |\n'
                  '  |     |\n'
                  '  |     O\n'
                  '  |      \n'
                  '  |      \n'
                  '__|__\n')
            print(f'Wrong guess. {limit - count} last guess remaining\n')
            time.sleep(2)
            clrscr()

        elif count == 5:
            print('   _____ \n'
                  '  |     |\n'
                  '  |     |\n'
                  '  |     |\n'
                  '  |     O\n'
                  '  |    /|\ \n'
                  '  |    / \ \n'
                  '__|__\n')
            print('Wrong guess. You are hanged!!!\n')
            print(f'The word was: {original_word}')
            time.sleep(3)
            clrscr()

            restart_game()
    if guessing_word == '_' * length:
        print(f'Congrats {name}! You have guessed the word {original_word} correctly!')
        time.sleep(3)
        clrscr()

        restart_game()
    elif count != limit:
        hangman()



#########################################################
# _____________________________________________________ #
#/                                                     \#
#|       STARTS THE GAME AND CLEANS THE CONSOLE        |#
#\____________________________________________________/ #
#                                                       #
#########################################################
clrscr() # Clears the Console to make it look clean and pretty

print('\n\n Welcome to Hangman game made by MoonieSerenity!\n')
time.sleep(1)
name = input('Please enter your name.\n')
time.sleep(0.75)
print(f'\nHello {name}!\nWishing you a pleasant game ahead.\n')
time.sleep(1)
while True:
    typeSelector = input('Please select the word type you would like to use between the following choices : "Adjectives", "Nouns", "Verbs".\n').casefold()
    if typeSelector == "adjectives" or typeSelector == "nouns" or typeSelector == "verbs":
        print(f'You have chosen the word type : {typeSelector}. Goodluck!\n')
        word_Type(typeSelector)
        time.sleep(2)
        clrscr()
        break
    else:
        print(f'You entered {typeSelector} which is not part of the given options. Please try again while providing an answer from the choices : "Adjectives", "Nouns", or "Verbs".\,n')

print('Get ready the game is about to start!\nTime for hangman!\n')
time.sleep(2.5)

clrscr() # Cleans the Console to make it look clean and pretty so that the rest of the code doesn't stagger

wordFetcher() # Gets the hangman word

hangman() # Starts the hangman game with the found word.