# generate a random list of numbers based on user input

import random

numbers = []
number = 0
how_many = input('How many numbers: ')
how_many = int(how_many)

while number < how_many:
   value = random.randint(1,100)
   if not(value in numbers):
      numbers.append(value)
      number += 1

print ("Your numbers:", numbers)




