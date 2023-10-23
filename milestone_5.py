import random

# A list of words that computer choses from
word_list = ['apple', 'mango', 'nectarine', 'pineapple', 'peach']

# Creating a class for a hangman game
class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list. It is 'private' to keep it in secret.  
    wrod_list: list
        A list of words from which computer picks a random word. 
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed.
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_'].
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_'].
    word_length: int
        The length of the random word picked by a computer.
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet.
    num_lives: int
        The number of lives the player has.
    list_letters: list
        A list of the letters that have already been tried.
    list_of_guesses: list
        A list of the guesses that have already been tried.

    Methods:
    -------
    update_guessed_word(guess)
        Updates word_guessed list and replaces '_' with a correctly guessed letters.
    check_guess(guess)
        Checks if the letter is in the word.
    ask_for_input()
        Asks the user to guess a letter.
    '''
    #Initialising the attributes of the class
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list           
        self.num_lives = num_lives           
        self.__word = random.choice(self.word_list) 
        self.word_length = len(self.__word)    
        self.num_letters = len(set(self.__word))    
        self.word_guessed = ["_" for position in range(self.word_length)]            
        self.list_of_guesses = []            

        print(f' Initial number of lives: {self.num_lives}')
        print(f' The word to be guessed: {self.word_guessed}')

    # Defining a method to update the guess list
    def update_guessed_word(self,guess):
        for position in range(self.word_length):        
            letter = self.__word[position]
            if letter == guess:
                self.word_guessed[position] = guess

    # Defining a method that firstly checks if the guess is correct. 
    # If it is, then runs update_guessed_word(guess) method and subtracts the number of unique letters.
    # If not, then subtracts the number of lives the player has.
    def check_guess(self, guess):
        if guess in self.__word:
            print(f'Good guess! {guess} is in the word.')
            for letter in self.__word:
                self.update_guessed_word(guess)
            self.num_letters -= 1                  
            print(f'Word to be guessed: {self.word_guessed}') 
        else:
            if guess not in self.__word:
                print(f'Sorry, {guess} is not in the word. Try again.')
                self.num_lives -= 1
                print(f'You have {self.num_lives} lives left.')


    # Defining a method for continuous user imput. 
    # Sets conditions of an input and rejects incorrect input
    # If conditions are met, it calls check_guess(guess) method and appends the list_of_guesses.
    def ask_for_input(self):
        while True:
            guess = input('Please, enter  a single letter: ').lower()
            if not guess.isalpha() or len(guess) != 1:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print(f'You already tried letter {guess}!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(f'List of your guesses: {self.list_of_guesses}')



# hangman = Hangman(word_list, 5)
# hangman.ask_for_input()
# print(hangman.list_of_guesses)

def play_game(word_list):
    # num_lives = 5
    game = Hangman(word_list, 5)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_lives > 0 and game.num_letters == 0:
            print('Congratulations. You won the game!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        

play_game(word_list)

