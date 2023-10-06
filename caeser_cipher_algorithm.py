alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(text, shift, direction):
    result_text = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            new_position = new_position % len(alphabet)
            result_text += alphabet[new_position]
        else:
            result_text += char
    return result_text

terminate_program = False
while not terminate_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type the message:\n").lower()
    shift = int(input("Type the shift:\n"))
    result = caeser(text, shift, direction)
    print(result)
    program_continue = input("If you want to continue type 'yes'. Otherwise type 'no'.\n").lower()
    if program_continue == "no":
        terminate_program = True
        print("The program was terminated.")