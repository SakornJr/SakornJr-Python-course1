import random

dice = random.randint(1, 6)

while True:
    guess_number = int(input('Guess the number of 1-6: '))
    
    if guess_number == dice:
        print('Good job')
    elif guess_number < dice:
        print("Try again", "greater than")
    elif guess_number > dice:
        print("Try again", "less than")    
   
        
        