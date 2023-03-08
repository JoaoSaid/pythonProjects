import os

game_dictionary = {}
game_on = True
clear = lambda: os.system('clear')

while game_on == True:
    name = input("What is your name\n")
    bid = int(input("What is your bid?\n"))
    game_dictionary[name] = bid
    others = input("There are other bidders?\n").lower()
    clear()
    if others == 'no':
        game_on = False

def game(game_info):
    highest_bid = 0
    for n in game_info:
        if game_info[n] > highest_bid:
            highest_bid = game_info[n]
            winner = n
    print(f"The auction ended.The highest bid was ${highest_bid} made by {winner} ")  

game(game_dictionary)

