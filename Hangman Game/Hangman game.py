import random
from words import words
import string

def GetValidWord(words):
    word = random.choice(words)  #Choses random word from the word list
    while '-' in word or ' ' in word:
        word = random.choice(words)       #Keeps words with spaces or -'s from being selected
    
    return word.upper()

def hangman():
    word = GetValidWord(words)
    wordLetters = set(word)    #Letters in the word
    alphabet = set(string.ascii_uppercase) 
    usedLetters = set() #Letters user has guessed
    lives = 7


    while len(wordLetters) > 0 and lives > 0:
        #letters used
        print('You have ', lives, ' lives left and used the letters: ', ' '.join(usedLetters)) #creates a string seperated by a space for 
        
        #What the current word is
        wordList = [letter if letter in usedLetters else '-' for letter in word]
        print('Current Word: ', ' '.join(wordList))


        userLetter = input ('Guess a letter: ').upper() #User input for letter selection
        print(userLetter)
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
            else:
                lives = lives - 1 #Remove one life
                print("Letter is not in word.\n")
                
        elif userLetter in usedLetters:
            print ('You have already used that character. Please try again.\n')
        else:
            print ('Invalid character. Please try again.\n')
    
    if lives == 0:
        print('You are dead. The word was', word)
    print("Congratulations! You guessed the word", word, 'correctly!')
    
hangman()

