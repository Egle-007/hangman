import random


# computers list of words that it chooses from
word_list = ['pear', 'mango', 'nectarine', 'orange', 'peach']
print(word_list)

# how to call a random ward 
word = random.choice(word_list)
print(word)     # Egle, delete the print later

# creating a hangman class which will use functions from milestone_3.py

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list      # a list of words from which computer picks a random word
        self.num_lives = num_lives      # user has 5 lives and looses one if chooses wrong answer
        self.word = None                # word to be guessed that was chosen by computer
        self.word_guessed = None        # list - a list of the letters of the word, with _ for each letter not yet guessed
        self.num_letters = None         # the number of UNIQUE letters in the word that have not been guessed yet
        self.list_of_guesses = []     #A list of the guesses that have already been tried.
    def check_guess(self, guess):
        guess = guess.lower()
        for letter in word:
            if letter == guess:
                print(f'Good guess! {guess} is in the word.')
            else:
                print(f'Sorry, {guess} is not in the word. Try again.')
    def ask_for_input(self):
        while True:
            guess = input('Please, enter  a single letter: ')#.lower()
            if not guess.isalpha() or len(guess) != 1:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
                    # self.list_of_guesses += letter 
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess) 
                print(self.list_of_guesses)
                
    
hangman = Hangman(word_list, 5)
hangman.ask_for_input()
print(hangman.list_of_guesses)

                
                
    
            
        

    

                
    
            
        

    
