#random number guessing game.

import random

#user_number = int(input("Enter a number between 1-20: "))
count = 0
user_number = 0
random_number = random.randint(1, 20)

while user_number != random_number:
    count += 1
    user_number = int(input("Enter a number between 1-20: "))
      
    if user_number < random_number:
        print("To low!")
        
    elif user_number > random_number:
        print("To high!")
    
    elif user_number == random_number and count == 1:
        print("Right on first try. Bonus Points!!")
        
    elif user_number == random_number:
        print(f"You guessed it! The number is {random_number}, you have guessed it in {count} attempts.")
        break