import random
from art import logo

chosen_number = random.randint(1, 100)

print(logo)
name = input("Welcome to the Number Guessing Game! What's your name? ")
print(f"Hey {name}, I'm thinking of a number between 1 and 100")

print(f"Psst, the correct answer is {chosen_number}")
CHOOSE = input("Choose a difficulty. Type 'easy' or 'hard': ")

tries = 0

def play(tries):
    attempts = False
    # while not tries > 10:
    while not attempts:
        tries -= 1
        guess = int(input("Make a guess: "))
        if guess > chosen_number:
            print("Too high")
        elif guess < chosen_number:
            print("Too low")
        elif guess == chosen_number:
            print(f"{chosen_number} is the correct answer. You Win!")
            attempts = True
        if guess != chosen_number:
            print("Guess again.")
            print(f"You have {tries} attempts remaining to guess the number")
            if tries == 0:
                print(f"You've run out of guess, you lose, the answer was {chosen_number}")
                attempts = True

def main():

    if CHOOSE == "easy":
        print("You have 10 attempts remaining to guess the letter")
        play(10)

    elif CHOOSE == "hard":
        print("You have 5 attempts remaining to guess the letter")
        play(5)

if  __name__ == "__main__":
    main()