print('''
                                      88           
                                ,d    88           
                                88    88           
88,dPYba,,adPYba,  ,adPPYYba, MM88MMM 88,dPPYba,   
88P'   "88"    "8a ""     `Y8   88    88P'    "8a  
88      88      88 ,adPPPPP88   88    88       88  
88      88      88 88,    ,88   88,   88       88  
88      88      88 `"8bbdP"Y8   "Y888 88       88 
''')

print('''=====WELCOME TO THE MATHS QUIZ=====
      You will be asked 3 questions,        
      let's see how many you can get right!
      ''')

count=0

if input('Do you want to play? (y/n): ').lower() == 'y':
    print('Great! Let\'s play!')
    
    ans = int(input("What is 615 + 374?"))
    if ans == 615 + 374:
        print("Correct! Next question...")
        count += 1
    else:
          print("Incorrect! Next question...")
    ans = int(input("What is 489 - 317?"))
    if ans == 489-317:
        print("Correct! Last question...")
        count += 1
    else:
          print("Incorrect! Last question...")
    ans = int(input("What is 23 x 7?"))
    if ans == 23*7:
        print("Correct! now let's see how many you got right...")
        count += 1
    else:
          print("Incorrect! now let's see how many you got right...")
    print(f"You have scored {count} out of 3!")
    print("Thanks for playing!")
else:
    print('That\'s a shame, maybe next time!')