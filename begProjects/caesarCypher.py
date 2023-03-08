print("Welcome to Caesar Cypher")
user_choice = input("Press (1) to encode , press (2) to decode.")
message = input("What is the message ?").upper()
shift = int(input("What is the shift number ?"))
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z''A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encode(message,shift):
    cypher = ''
    for letter in message:
        alphabet_positions = alphabet.index(letter)
        new_position = alphabet_positions + shift
        new_letter = alphabet[new_position]
        cypher += new_letter
    print(f"The encoded text is {cypher}")

def decode(message,shift):
    decoded_text = ''
    for letter in message:
        alphabet_positions = alphabet.index(letter)
        new_position = alphabet_positions - shift
        new_letter = alphabet[new_position]
        decoded_text += new_letter   
    print(f'The decoded text is {decoded_text}')

if user_choice == '1':
    encode(message,shift)
else:
    decode(message,shift)