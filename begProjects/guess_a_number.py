import random

range_input = int(input("What is the higher number possible for the guessing game?"))

def range_guess(x):
    random_number = random.randint(1,x)
    guess = int(input("Try a number: "))
    while(random_number != guess):
        if guess > random_number:
            print("The secret number is lower")
        elif guess < random_number:
            print("The secret number is higher")
        guess = int(input("Try a number: "))
    print("You found the number !")     

range_guess(range_input)




