from art import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for char in start_text:
        if char in alphabet:
            if cipher_direction == "encode":
                position = alphabet.index(char)
                new_position = position + shift_amount
                new_letter = alphabet[new_position]
                end_text += new_letter
            elif cipher_direction == "decode":
                position = alphabet.index(char)
                new_position = position - shift_amount
                new_letter = alphabet[new_position]
                end_text += new_letter
            else:
                print("Invalid type!")
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")
print(art)

should_end = False
while not should_end: 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # print(shift)
    shift = shift % 25  # number of alphabets from 0 - 25
    # print(shift)
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
    else:
        print("wrong input")
        # print(restart)
            

