alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

from cipher_art import logo
print(logo)

should_end = False
while not should_end:

  direction = input("Please type 'encode' to encrypt and type 'decode' to decrypt: \n")
  text = input("Please type your message: \n").lower()
  shift = int(input("Please type the shift number:\n"))
  shift = shift % 26

  caesar(start=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Please type 'yes' if you want to use the service again, else type 'no': \n")
  if restart == "no":
    should_end = True
    print("Thanks a lot for using the service. Have a nice day!")
    


