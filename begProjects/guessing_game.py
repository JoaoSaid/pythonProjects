import random

def number_to_find():
    """Choose a number for the game """
    numbers_list = []
    for number in range(0,101):
        numbers_list.append(number)
    game_number = random.choice(numbers_list)
    return game_number
def guessing(guess_number,stored_number):
    """Compare the numbers and give a feedback"""
    if guess_number == stored_number:
        print("You won !")
        return True
    elif guess_number > stored_number:
        return print("Too high")
    else:
        return print("Too low")
def difficulty(user_answer):
    """Apply the difficulty chosen by the user"""
    if user_answer == 'easy':
        attemps = 12
    elif user_answer == 'medium':
        attemps = 8
    else:
        attemps = 5
    return attemps

def welcome():
    """Print some phrases for the user"""
    print("Welcome to the Guessing Game !")
    print("Find the number between 0 and 100")
    print("You can play in easy,medium,and hard modes")

welcome()
answer = input("What is the difficulty that you want to play?\n").lower()
game_attemps = difficulty(answer)
computer_number = number_to_find()
while game_attemps > 0:
    guess = int(input("Guess a number: "))
    if guessing(guess,computer_number) == True:
        break
    else:
        game_attemps -= 1
        game_result = False
if game_attemps == 0:
    print("You lose !")

