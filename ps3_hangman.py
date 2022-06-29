# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of 
    lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord 
    are in lettersGuessed;
    False otherwise
    '''
    for letter in secretWord :
        if letter in lettersGuessed : continue
        else:
            return False
    return True
        



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that 
    represents what letters in secretWord have been
    guessed so far.
    '''
    returnString = ""
    for letter in secretWord :
        if letter in lettersGuessed :
            returnString = returnString + letter
        else:
            returnString = returnString + '_'
    return returnString



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what 
    letters have not yet been guessed.
    '''
    # String to output and edit 
    availableL = 'abcdefghijklmnopqrstuvwxyz'
    for letter in lettersGuessed :
        if letter in availableL :
            availableL = availableL.replace(letter, "")
    
    return availableL

def secretWord():
    # Loading the secret word
    SW = chooseWord(loadWords())
    print(SW)
    return SW

def messageRequest(guessesLeft, LettersGuessed):
    print('You have ' + str(guessesLeft) + ' guesses left.')
    print('Available letters: ' + str(getAvailableLetters(LettersGuessed)))
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each 
    guess about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    SWl = len(secretWord)
    # The allowance of guesses for each game
    guessLeft = 8
    
    # List to store letters guessed so far
    guessedLetters = []
    
    #List of available letters to check if input is valid at all
    availableL = 'abcdefghijklmnopqrstuvwxyz'

    # ======================
    # The start of the game.
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(SWl) + ' letters long.')
    
    while isWordGuessed(secretWord, guessedLetters) == False:
        if guessLeft == 0:
            print("-----------")
            return print("Sorry, you ran out of guesses. The word was " + str(secretWord))
        print("-----------")
        messageRequest(guessLeft, guessedLetters)
        l = str(input('Please guess a letter: '))
        
        if l not in availableL:
            print("Sorry, I don't understand. Please use lowercase english letters only.")  
            continue
        elif l in guessedLetters :
            print("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, guessedLetters)))
        elif l in secretWord :
            guessedLetters.append(l)
            print('Good guess: ' + str(getGuessedWord(secretWord, guessedLetters)))
        elif l not in secretWord :
            guessedLetters.append(l)
            guessLeft -= 1
            print("Oops! That letter is not in my word: " + str(getGuessedWord(secretWord, guessedLetters)))
    print("-----------")
    return print("Congratulations, you won!")



    
 
print(hangman(secretWord()))



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
