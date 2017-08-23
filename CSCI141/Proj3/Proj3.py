# Proj3.py
# Thomas Blackwell
# Compsci 141

# This program contains four word games. The four games are each contained in 
# their own procedures. A while loop prompts users to select a game type until
# 'q' or 'Q' is inputted, at which the program terminates and a quit message is
# displayed. 

# The first game, which is accessed by an input of 'a' or 'A', 
# finds and prints all words of the length specified, that contain 
# only one vowel, and lack a the letter specified by the user. This game is 
# defined as the procedure "lengthAndVowels."

# The second program, accessed by an input of 'b' or 'B', finds and prints all 
# words containing the letters of a specified word (without regards to order, 
# including repeated characters) with a maximum length as specified by the user. 
# This game is defined as the procedure "sameLettersFinder." 

# The third program finds all words that contain all but one of a user-inputted
# string of characters. For instance, if one typed acuzitylas, the program would
# print "causality" as one of the valid words. 
# This program is accessed by an input of either 'c' or 'C' This game is defined
# as the procedure "allButOne."

# The fourth program finds the two U.S. state capitals that have a prefix that 
# is the name of the month. It is accessed by an input of 'd' or 'D', and prints
# the names of the capitals that fit the criteria. This game is defined as the 
# procedure "capitalMonthNames."

# This program relies on two text files: dictionary.txt and capitals.txt. 
# dictionary is a fairly comprehensive list of words in alphabetical order, 
# while capitals is a list of United States State Capital cities. Dictionary is
# used in games A, B, and C. Game D, however, uses capitals.txt. 


# assigns list of a months, opens the dictionary file

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',\
'August', 'September', 'October', 'November', 'December']

dictionary = open("dictionary.txt",'r')


def lengthAndVowels(dictionary):
    
    # This procedure is game A as described in the prologue. This procedure
    # prompts the user for a word length, and a letter to exclude, and echo
    # prints the inputs. For every word in the dictionary (using a for loop),
    # the procedure checks the length of the word. If it is not of the specified
    # length, the word is skipped. Words of valid length are evaluated for
    # the presence of vowels, and counts the number of vowels. If the count is
    # equal to one, and the letter to exclude is not present in the word, the
    # word is printed. 
    
    length = int(input("Please enter the word length you are looking for: "))
    print(length)
    
    letter = input("Please enter the letter you'd like to exclude: ").lower()
    print(letter,'\n')
    
    # vowels string created to check for vowel presence. 
    
    vowels = "aeiou"
    numberOfWords = 0
    
    for word in dictionary:
        numberOfVowels = 0
        if len(word.rstrip())!= length:
            continue
        for char in word:
            if char in vowels:
                numberOfVowels += 1
        if numberOfVowels == 1 and letter not in word:
            print(word, end = '')
            numberOfWords += 1
            
    if numberOfWords == 0:
        print('There are no words that fit this criteria.')
        
    print()

        
def sameLettersFinder(dictionary):
    
    # This procedure is game B as described in the prologue. This procedure
    # prompts the user for a word to find matches for, a max length for the 
    # matches, and echo prints the inputs. The procedure checks every word in
    # dictionary (using a for loop), and skips words with a length greater than
    # the max length. If the word is of proper length, the procedure checks for 
    # the presense of characters of the inputted word in the dictionary word, 
    # and counts them. If the count is identical, then the word is printed. This 
    # uses a ..replace(), in which the found character is replaced by a blank
    # space in the dictionary word once to account for repeated characters. 
    
    firstWord = input("Enter word: ").lower()
    print(firstWord)
    
    maxLength = int(input("What is the maximum length of the words you want: "))
    print(maxLength,'\n')
    
    numberOfWords = 0
    firstWordLetters = len(firstWord.rstrip())
    
    for word in dictionary:
        
        # a copy of the word is created so that the original word is printed
        # rather than the multilated version produced by the .replace(). 
        
        sharedLetters = 0
        savedWord = word 

        if len(word.rstrip()) > maxLength:
            continue
        
        for char in firstWord:
            if char in word:
                word = word.replace(char,'',1)
                sharedLetters += 1
                
        if sharedLetters == firstWordLetters:
            print(savedWord, end = '')
            numberOfWords += 1
            
    if numberOfWords == 0:
        print("There are no words that fit this criteria")
    print()
                

def allButOne(dictionary):
    
    # This procedure is game C as described in the prologue. This procedure 
    # prompts users for a string of characters, echo prints the input, and then
    # checks all words in the dictionary for if they contain all but one of 
    # these characters. It does this by checking all words for shared characters
    # and counting the number of shared characters, with a for loop.
    # If the number of shared characters is found to be one less than the length
    # of the inputted string, then the word is printed. If no words are found, a 
    # message stating so is printed. 
    
    characters = input("Please enter the characters you are looking for: ")
    print(characters,'\n')
    
    characterCount = len(characters)
    numberOfWords = 0
    
    for word in dictionary:
        
        sharedLetters = 0
        savedWord = word
        
        for char in characters:
            if char in word:
                word = word.replace(char,'',1)
                sharedLetters += 1
                
        if sharedLetters == characterCount - 1:
            print(savedWord, end = '')
            numberOfWords += 1
            
    if numberOfWords == 0:
        print("There are no words that fit this criteria")
        
    print()    
    
    
def capitalMonthNames():
    
    # This procedure is game D as described in the prologue. For every capital
    # in capitals.txt, the procedure checks if an individual month name is
    # present in the name of the capital. If a month name is found, the capital
    # is is found in is printed. Capitals is opened and closed within this 
    # procedure. Nothing is passed to this procedure. 
    
    capitals = open("capitals.txt",'r')
    
    
    monthList = months
    capitalCount = 0
    
    for capital in capitals:
        for month in monthList:
            if month in capital:
                print(capital,end='')
                capitalCount += 1
                
    if capitalCount == 0:
        print("There are no capitals that fit this criteria")
        
        # Above should never print but is included to match project guidelines
        
    print()
    capitals.close()
    
# Main Menu. This presents users with a 5 option menu, and loops until 'q' or 
# 'Q' is inputted. Additionally, this loop contains a .seek(0), which returns
# the input pointer for dictionary.txt to the beginning of the file to ready it
# for the next game. gameType is assigned to prevent errors. 

gameType = ''
print("Let's play a game\n")

while gameType != "q":
    
    dictionary.seek(0)
    print("""Choose which game you want to play
a) Find words with only one vowel and excluding a specific letter
b) Find words containing all the letters of another word with a maximum length
c) Find words containing all but one letter of a given string
d) Find state capitals starting with the name of a month
q) Quit

""")
    # prompts user for game type, lowers input, and echo prints input. 

    gameType = input("Enter a choice: ").lower()
    print(gameType,"\n")
    
    # The following if, and three elif statements check for the gameType, and 
    # call the procedures matching the gameType if the user input matches the 
    # letter of the gameType. For the dictionary related games, dictionary is
    # passed as an argument. Nothing is passed for capitals. Q only displays
    # a quit message. 
    
    if gameType == 'a':
        lengthAndVowels(dictionary)
    
    elif gameType == 'b':
        sameLettersFinder(dictionary)
    
    elif gameType == 'c':
        allButOne(dictionary)
    
    elif gameType == 'd':
        capitalMonthNames()
        
    elif gameType == 'q':
        print('Thanks for playing')
    
    # The following prints an error message upon an invalid input
        
    elif gameType not in 'abcdq':
        print("You've entered an incorrect choice. Try again\n")
        
# closes the program
dictionary.close()
