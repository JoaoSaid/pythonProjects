import random

def play():
    my_choice = input("Press (R) for rock , (S) for scissors or (P) for paper \n").lower()

    computer_choice = random.choice(['r','s','p'])
    
    if my_choice == computer_choice:
        return "It\'s a tie!"
    
    if win(my_choice,computer_choice):
        return "You won !"
    else:
        return "You lost !"

def win(x,y):
    if (x == 'r' and y == 's') or (x == 's' and y == 'p') or (x == 'p' and y == 'r'):
        return True
print(play())    


