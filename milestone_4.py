import random

# computers list of words that it chooses from
word_list = ['apple', 'mango', 'nectarine', 'pineapple', 'peach']

# creating a hangman class which will use functions from milestone_3.py
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list           # a list of words from which computer picks a random word
        self.num_lives = num_lives           # user has 5 lives and looses one if chooses wrong answer
        self.word = random.choice(word_list) # word to be guessed that was chosen by computer
        self.num_letters = len(set(self.word))    # the number of UNIQUE letters in the word that have not been guessed yet
        self.word_guessed = ["_" for position in range(len(self.word))]               # list - a list of the letters of the word, with _ for each letter not yet guessed
        self.list_of_guesses = []            #A list of the guesses that have already been tried.
    
    def check_guess(self, guess):
        for letter in self.word:
            if letter == guess:
                print(f'Good guess! {guess} is in the word.')
                for position in range(self.num_letters):        # this block updates word_guessed list and replaces '_' with a guessed letters
                    letter = self.word[position]
                    if letter == guess:
                        self.word_guessed[position] = letter
                        print(f'Word to be guessed: {self.word_guessed}') # to be deleted 
                self.num_letters -= 1                   # and subtracts a unique number of letters when the guess is right
        if guess not in self.word:
            print(f'Sorry, {guess} is not in the word. Try again.')
            self.num_lives -= 1   
            print(f'You have {self.num_lives} lives left.') 
          
    
    def ask_for_input(self):
        while True:
            guess = input('Please, enter  a single letter: ').lower()
            if not guess.isalpha() or len(guess) != 1:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess) 
                print(self.list_of_guesses)
                

    
hangman = Hangman(word_list, 5)
hangman.ask_for_input()
print(hangman.list_of_guesses)

                
                
    
            
        

    

                
    
            
        

    
