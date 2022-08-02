from art import logo, vs
from game_data import data
import random
import os

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right.
       
       The code says if A has more followers and they guessed A then return True
       but if B has more followers and they guessed B then return True and if
       the opposite happens, then return False"""
    if a_followers > b_followers:
        return guess == "a"  
    else:
        return guess == "b"

def play():
    print(logo)
    score = 0
    game_should_continue = True
    account_b = random.choice(data)

    while game_should_continue:
        account_a = account_b
        account_b = random.choice(data)
        if account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_follower_count = account_a["follower_count"] 
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        os.system("cls")
        print(logo)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

def main():
    play()
    while input("Play Again? (y/n) ").lower() == "y":
        os.system("cls")
        play()
if  __name__ == "__main__":
    main()