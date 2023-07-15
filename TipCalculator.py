print("Welcome to the tip calculator. ")

bill = float(input("What was the total bill? ₹"))

per = float(input("What percent of of you bill should go to tip? Enter between 0 to 20: "))

people = int(input("How many people are splitting the bill? "))

total = bill + (bill * per) / 100

each = total / people

print(f"Each person should pay ₹{round(each, 2)}/- \n Thank you for using our service, do visit again!! ")

