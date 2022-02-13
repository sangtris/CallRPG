import random
import math 

def get_random_number(min, max):
    number=min+random.random()*(max-min)
    number=math.floor(number)
    return number

validCharacters = "0123456789qwertzuiopasdfghjklyxcvbnm"
random_password = ""

for x in range(0, 9):
    number = get_random_number(0, len(validCharacters))
    random_password = random_password + validCharacters[number]

print(random_password)