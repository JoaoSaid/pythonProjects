import random

numbers = ['0','1','2','3','4','5','6','7','8','9']
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
symbols = ['!','@','#','$','%','^','^','&','*']

print('Welcome to the password generator')
letters_required = int(input('How many letters do you want ?\n'))
symbols_required = int(input('How many symbols do you want ?\n'))
numbers_required = int(input('How many number do you want?\n'))

chosen_letters = ''
chosen_symbols = ''
chosen_numbers = ''

password = []

for letter in range(0,letters_required):
    chosen_letters = random.choice(letters)
    password.append(chosen_letters)

for symbol in range(0,symbols_required):
    chosen_symbols = random.choice(symbols)
    password.append(chosen_symbols)

for number in range(0,numbers_required):
    chosen_numbers = random.choice(numbers)
    password.append(chosen_numbers)

final_password = ''

print("Your password is :")
for digit in range(0,len(password)):
    final_password += password[digit]
print(final_password)



