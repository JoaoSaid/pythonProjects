print("Welcome to the Tip Calculator")
bill =float(input("What is the total bill ?\n"))
percentage = input("What is the percentage you would like to give ?\n")
split = int(input("How many people going to split the bill ?\n"))

tip_percentage = "1." + percentage

tip_percentage_formatted = float(tip_percentage)

total_tip = bill * tip_percentage_formatted

total_for_person = total_tip / split

print(f"Each person should pay ${round(total_for_person,2)}")