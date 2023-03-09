import random

cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]

user_cards = []
computer_cards = []
drawing = 0

game_on = input("Do you want to play ?")

def draw_cards(cards):
    return random.choice(cards)

if game_on == 'yes':
    while drawing == 2:
        user_cards.append(draw_cards(cards))
        computer_cards.append(draw_cards(cards))
        drawing += 1
    