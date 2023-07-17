import random

print('''
                                                                                                               
I8,        8        ,8I 88888888888 88          ,ad8888ba,   ,ad8888ba,   88b           d88 88888888888  
`8b       d8b       d8' 88          88         d8"'    `"8b d8"'    `"8b  888b         d888 88           
 "8,     ,8"8,     ,8"  88          88        d8'          d8'        `8b 88`8b       d8'88 88           
  Y8     8P Y8     8P   88aaaaa     88        88           88          88 88 `8b     d8' 88 88aaaaa      
  `8b   d8' `8b   d8'   88"""""     88        88           88          88 88  `8b   d8'  88 88"""""      
   `8a a8'   `8a a8'    88          88        Y8,          Y8,        ,8P 88   `8b d8'   88 88           
    `8a8'     `8a8'     88          88         Y8a.    .a8P Y8a.    .a8P  88    `888'    88 88           
     `8'       `8'      88888888888 88888888888 `"Y8888Y"'   `"Y8888Y"'   88     `8'     88 88888888888  
''')



print("Welcome to the Rock Paper Scissors Game, where you will be playing against the computer. \n")

print("Type your choice and press enter to play. \n")

print("Enter 1 for Rock, 2 for Paper, and 3 for Scissors. \n")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = int(input("So, what is your choice? "))
choice = player_choice - 1
choices = [rock, paper, scissors]

print(choices[choice])

if(choice > 2):
    print("Please enter a valid choice the next time you run the game. \n")
    exit()
else:
    comp = random.randint(0,2)
    print("The computer chose: ")
    print(choices[comp])
    if (choice == comp):
        print("It's a tie! \n")
        print("You chose " + choices[choice] + " and the computer chose " + choices[comp] + ". \n")
    elif choice == 0 and comp == 2:
        print("You win!")
    elif comp == 0 and choice == 2:
        print("You lose")
    elif comp > choice:
        print("You lose")
    elif choice > comp:
        print("You win!")
    elif comp == choice:
        print("It's a draw")