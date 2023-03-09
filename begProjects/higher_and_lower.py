from higher_and_lower_game_data import data
import random
def welcome():
    """Print some explanations"""
    print("Welcome to the higher and lower game")
    print("Two accounts will appear, and you will guess which has more Instagram followers")

def generate_account():
    """Generate random accounts"""
    account = random.choice(data)
    return account

def verify_ambiguity(first_generation,second_generation):
    """Verification if the first variable is equal to the second"""
    if first_generation == second_generation:
        return True
    else:
        return False
        
def display_names(first_name,first_description,second_name,second_description):
    """Display the name of accouns who will be part of the game"""
    return print(f"Press A for {first_name},{first_description} or press B for {second_name},{second_description}")

def game():
    """Execute the game"""
    welcome()
    game_on = True
    points = 0
    first = generate_account()
    while game_on == True:
        second = generate_account()
        ambiguity = verify_ambiguity(first,second)
        while ambiguity == True:
            second = generate_account()
        display_names(first.get("name"),first.get("description"),second.get("name"),second.get("description"))
        user_choice = input().lower()
        if user_choice == "a" and first.get("follower_count") > second.get("follower_count"):
            print("You got a point !")
            print(f"Your score: {points + 1}")
            points += 1
        elif user_choice == "b" and second.get("follower_count") > first.get("follower_count"):
            print("You got a point !")
            print(f"Your score: {points + 1}")
            points += 1
        elif user_choice == "b" and second.get("follower_count") > first.get("follower_count"):
            print("You lose!")
            print(f"Your score was {points} ")
            game_on = False
        else:
            print(f"Your score was {points}")
            game_on = False
game()
