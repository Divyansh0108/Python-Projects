from turtle import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

print("Ladies and gentlemen, welcome to the secret auction program.")

bids = {}
finished = False

def highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ₹{highest_bid}")


while not finished:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: ₹"))
    bids[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_bidders == "no":
        finished = True
        highest_bidder(bids)
    elif more_bidders == "yes":
        clear()