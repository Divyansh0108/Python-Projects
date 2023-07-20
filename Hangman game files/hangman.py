import random
from hangman_word_list import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end = False
number_of_lives = 6

from hangman_ascii_art import logo
print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end:
    guessed_letter = input("Please guess a letter:- ").lower()

    if guessed_letter in display:
        print(f"You've already guessed {guessed_letter} brooo, keep your head in the game. ")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = letter

    if guessed_letter not in chosen_word:
        print(f"You guessed {guessed_letter}, which is not in the word. YOU LOST A LIFE LOL!!!!")
        
        number_of_lives -= 1
        if number_of_lives == 0:
            end = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end = True
        print("You win.")
        
    from hangman_ascii_art import stages
    print(stages[number_of_lives])