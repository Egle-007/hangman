import random
# computers list of words that it chooses from
word_list = ['pear', 'mango', 'nectarine', 'orange', 'peach']
print(word_list)

# how to call a random ward 
word = random.choice(word_list)
print(word)     # Egle, delete the print later


# Task 1
# Iteratively checking if the input is valid
# while loop to do checks if the user input just one character 
# and that the chosen characted is a letter
# while True:
#     guess = input('Please, enter  a single letter: ').lower()
#     if len(guess) == 1 and guess.isalpha():
#         break
#     else:
#         print('Invalid letter. Please, enter a single alphabetical character.')


# Task 2
# here checking if the guessed letter is in the word
# for letter in word:
#     if letter == guess:
#         print(f'Good guess! {guess} is in the word.')
#     else:
#         print(f'Sorry, {guess} is not in the word. Try again.')
# at the moment it checks every single letter and gives result for every single letter
# and if it doesn't match it gives else result until it matches or is finished


# Task 3
# defining a guess check function to check if the guessed letter is in the word
def check_guess(guess):
    guess = guess.lower()
    for letter in word:
        if letter == guess:
            print(f'Good guess! {guess} is in the word.')
        else:
            print(f'Sorry, {guess} is not in the word. Try again.')
        
# defining a a function for user input
def ask_for_input():
    while True:
        guess = input('Please, enter  a single letter: ').lower()
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess)

ask_for_input()