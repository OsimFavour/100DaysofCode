import random

rock =''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
     _______
---'    ____)____
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


game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
choose = game_images[user_choice]
print(choose)

computers_choice = random.randint(0, 2)
print("Computer choose: ")
print(game_images[computers_choice])

if user_choice >= 3 or user_choice < 0:
    print("Invalid number! You lose")
elif user_choice == 0 and computers_choice == 2:
    print("You win!")
elif computers_choice == 0 and user_choice == 2:
    print("You lose!")
elif user_choice > computers_choice:
    print("You win!")
elif computers_choice > user_choice:
    print("You lose!")
elif user_choice == computers_choice:
    print("That's a draw")