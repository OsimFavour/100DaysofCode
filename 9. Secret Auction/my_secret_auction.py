import os
from art import logo

print(logo)
print("Welcome to the secret auction program.")

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price 
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    os.system("cls")
    if should_continue == "yes":
        bids.update({name:price})
    elif should_continue == "no":
        max_number = 0
        winner = ""
        for key, value in bids.items():
            if value > max_number:
                max_number = value
                winner = key
        print(f"The winner is {winner} with a bid of ${max_number}")
        bidding_finished = True
    else:
        print("Wrong Input")


