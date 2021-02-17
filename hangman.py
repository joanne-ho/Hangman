import random

word_file = open("words_alpha.txt","r")
contents = word_file.readlines()
words = []
for word in contents:
    words.append(word)

missedLetters = []
correctLetters = []
MAX_WRONG_GUESSES = 20


def getRandomWord(wordList): #fetches random word from the text file
    wordIndex=random.randint(0,len(wordList)-1)
    return wordList[wordIndex]

secretWord = getRandomWord(words)

def displayLetters(missedLetters, correctLetters, secretWord):
    print("Wrong guesses: " + str(missedLetters))
    print("Correct guesses: " + str(correctLetters))
    print("You have " + str(MAX_WRONG_GUESSES-len(missedLetters)) + " guesses left.")
    blanks = "_ " * (len(secretWord)-1)

    for i in range(len(secretWord)-1):
        if secretWord[i] in correctLetters: #checks if a letter has already been guessed correctly
            blanks = blanks[:2*i] +secretWord[i] + blanks[2*i+1:]

    print(blanks)

def getGuess():
    while True:
        print("Guess a letter")
        guess = input()
        guess = guess.lower()
        if len(guess)!=1: #if user accidentally enters more than one letter
            print("Please enter a single letter")
        elif guess in missedLetters or guess in correctLetters:
            print("You have already guessed this letter")
        elif not guess.isalpha():
            print("Please enter a letter of the alphabet")
        else:
            return guess

finishedGame = False

while not finishedGame:
    displayLetters(missedLetters,correctLetters, secretWord)

    guess = getGuess()

    if guess in secretWord: #if the user correctly guesses a letter
        correctLetters.append(guess)

        foundAllLetters = True
        for i in range((len(secretWord))-1):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters:
            print("Well done! You have guessed the secret word, " + secretWord + ". Would you like to play again?")
            playAgainResponse = input()
            if playAgainResponse.lower() == "yes" or playAgainResponse.lower() == "y":
                missedLetters = []
                correctLetters = []
                secretWord = getRandomWord(words)
            else:
                finishedGame = True

    else:
        missedLetters.append(guess)
        if len(missedLetters) > MAX_WRONG_GUESSES: #if the user has run out of guesses
            print("You have run out of guesses. The correct word was " + secretWord + ". Would you like to play again?")
            playAgainResponse = input()
            if playAgainResponse.lower() == "yes" or playAgainResponse.lower() == "y":
                missedLetters = []
                correctLetters = []
                secretWord = getRandomWord(words)
            else:
                finishedGame = True




