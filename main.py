# Hour of Code HK - Python Lesson 7
# Author: Anson
# Date: 28 March, 2021

# package used
import random
import string

# Prepare keywords
adjectives = ['sleepy','slow','smelly','wet']

nouns = ['apple','dinosaur','ball','basketball','pi-day']

# forever loop
while True:
  adj = random.choice(adjectives)
  noun = random.choice(nouns)
  number = random.randrange(0,100)
  special_char = random.choice(string.punctuation)

  password = adj + noun + str(number) + special_char
  print('Your new password is: %s' % password)

  # Check user feedback
  response = input('Would you like another password? Type Y or N: ')
  if response == 'n':
    break
