#modules for program
import random
import string

#lists
adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'fluffy', 'white', 'proud', 'brave']

nouns = ['apple', 'dinosaur', 'ball', 'toaster', 'goat', 'dragon', 'hammer', 'duck', 'panda']

print('Welcome to Password Picker!')

# randomly selecting a word from the lists
adjective = random.choice(adjectives)
noun = random.choice(nouns)
number = random.randrange(0, 100) #randrange is a function imported from 'random', as is 'choice'
special_char = random.choice(string.punctuation) #punctuation is a constant from 'string' module

# generating a *new* password
password = adjective + noun + str(number) + special_char # str(number) is converting the integer to a string

print('Your new password is: %s' %password)