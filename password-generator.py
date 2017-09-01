# A simple password generator

import random
import string

def gen_password(length):
	chars_list = list(string.ascii_letters + string.digits)
	genpass = "".join([random.choice(chars_list) for x in range(length)])
	print(genpass)

how_many = int(input("How many passwords to generate: "))
how_long = int(input("How long should passwords be: "))
counter = 0

while counter < how_many:
	my_password = gen_password(how_long)
	counter = counter + 1
