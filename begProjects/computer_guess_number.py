import random

range = int(input("What is the higher number possible for the guessing game ?"))

def guess(x):
    low = 1
    high = x
    answer = ''
    while answer != 'c': 
        if low != high:
            pc_guess = random.randint(low,high)
        else:
            pc_guess = high
        print(f"The pc guess is {pc_guess}")
        answer = input("If the computer guess is higher than the secret number press (H) ," +
            "if the computer guess is lower than the secret number press(L) and" + 
               "if the computer guess is correct press (C)").lower()
        if answer == 'h':
            high = pc_guess - 1
        elif answer == 'l':
            low = pc_guess + 1
    print("The computer guess is correct !")

guess(range)
            
    