import random
from art import logo

EASY_LEVEL_TRIES = 10
HARD_LEVEL_TRIES = 5

def check_number(guess, chosen_number):
    if guess > chosen_number:
        return "Too high"
    elif guess < chosen_number:
        return "Too low"
    elif guess == chosen_number:
        return f"{chosen_number} is the correct answer. You Win!"
    

def set_difficulty():
    choose = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if choose == "easy":
        return EASY_LEVEL_TRIES
    elif choose == "hard":
        return HARD_LEVEL_TRIES

def play():
    chosen_number = random.randint(1, 100)
    print(logo)
    name = input("Welcome to the Number Guessing Game! What's your name? ")
    print(f"Hey {name}, I'm thinking of a number between 1 and 100")
    
    tries = set_difficulty()
    attempts = False
    while not attempts:
        tries -= 1
        guess = int(input("Make a guess: "))
        print(check_number(guess, chosen_number))
        if tries == 0:
            print(f"You've run out of guess, you lose, the answer was {chosen_number}")
            attempts = True   
        elif guess != chosen_number:
            print("Guess again.")
            print(f"You have {tries} attempts remaining to guess the number")
        elif guess == chosen_number:
            attempts = True

play()
        