import collections
import random

wrongGuesses = -1
usedLetters = []

HANGMAN_PICS = ['''
       +---+
           |
           |
           |
          ===''', '''
       +---+
       O   |
           |
           |
          ===''', '''
       +---+
       O   |
       |   |
           |
          ===''', '''
       +---+
       O   |
      /|   |
           |
          ===''', '''
       +---+
       O   |
      /|\  |
           |
          ===''', '''
       +---+
       O   |
      /|\  |
     /     |
         ===''', '''
       +---+
       O   |
      /|\  |
      / \  |
          ===''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret ' \
        'fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon ' \
        'python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad ' \
        'trout turkey turtle weasel whale wolf wombat zebra'.split()


def intro():
    print('Welcome to hangman! I will choose a secret word and have you guess the letters one by one until you either '
          'win or the man dies, goodluck!')


def getRandomWord():
    randWord = random.choice(words)
    # print(randWord)
    return randWord


def showDrawingAndBlanks(WordAsList, blankList):
    print(HANGMAN_PICS[0])
    print(blankList)
    print(usedLetters)


def CreateBlanks(getWord, blankList):
    # getWord.split()
    for letter in getWord:
        blankList.append('_')

    return blankList


def UpdatedDrawingAndBlanks(blankList, usedLetters, wrongGuesses):
    if wrongGuesses <= 5:
        print(HANGMAN_PICS[wrongGuesses + 1])
        print(blankList)
        print('used letters: ')
        print(usedLetters)
        return wrongGuesses


def guessLetter(WordAslist, blankList):
    while True:
        print('guess a letter')
        guess = str(input())
        global wrongGuesses
        if guess in WordAsList and WordAsList.count(guess) == 1:
            print("correct you have guessed the correct letter")
            temp = WordAsList.index(guess)  # this value stores the the index of the character that was entered at
            # where the char is in the WordAsList
            blank = '_'
            blankList.pop(temp)
            blankList.insert(temp, guess)
            usedLetters.append(guess)
            UpdatedDrawingAndBlanks(blankList, usedLetters, wrongGuesses)

        elif guess in blankList or guess in usedLetters:
            print("you have already entered this letter, please try another letter")
            guessLetter(WordAsList, blankList)
        elif guess in WordAsList and WordAsList.count(guess) > 1:
            print("correct you have guessed the correct letter")
            start_at = -1
            locs = []
            usedLetters.append(guess)
            while True:
                try:
                    loc = WordAsList.index(guess,
                                           start_at + 1)  # here we will find the first location of guess in WordAsList
                    blankList.pop(loc)
                    blankList.insert(loc, guess)
                except ValueError:
                    break
                else:
                    locs.append(loc)  # next time the code loops, we will update the location to the newest location
                    start_at = loc

            #print(locs)
            UpdatedDrawingAndBlanks(blankList, usedLetters, wrongGuesses)
        if blankList == WordAsList:
            return blankList, WordAsList

        elif guess not in WordAsList:
            print("Oh no, you guessed the wrong letter")
            wrongGuesses += 1
            usedLetters.append(guess)
            UpdatedDrawingAndBlanks(blankList, usedLetters, wrongGuesses)

        if wrongGuesses == 5:
            return wrongGuesses


def convertWordToList(getWord):
    list1 = []
    list1[:0] = getWord
    # print(list1)
    return list1


def checkIfWon(blankList, WordAsList):
    if collections.Counter(blankList) == collections.Counter(WordAsList):
        print("you win, good job!")
        usedLetters.clear()

    else:
        return blankList, WordAsList


def checkIfLost(wrongGuesses):
    if wrongGuesses == 5:
        print("you have lost and the man was hanged!")
        print('the secret word was :' + getWord)
        usedLetters.clear()
        return True


playAgain = 'yes'

while playAgain == 'yes':
    intro()
    blankList = []
    getWord = getRandomWord()
    WordAsList = convertWordToList(getWord)
    CreateBlanks(WordAsList, blankList)
    showDrawingAndBlanks(WordAsList, blankList)
    guessLetter(WordAsList, blankList)
    checkIfWon(blankList, WordAsList)
    checkIfLost(wrongGuesses)
    print("do you want to play again? (yes or no)")
    playAgain = input()
    if playAgain == 'y' or 'yes':
        continue
    else:
        break
