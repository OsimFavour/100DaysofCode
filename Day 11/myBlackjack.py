import random
import os
from art import logo

def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)       
    return card

def calculate_score(number):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(number) == 21 and len(number) == 2:
        return sum(number)
    if 11 in number and sum(number) > 21:
        number.remove(11)
        number.append(1)
    return sum(number)

def compare(user_score, computer_score):
    if computer_score == user_score:
        return "That's a draw😇"
    elif computer_score == 21:
        return "BlackJack! Dealer wins, You lose!😢"
    elif user_score == 21:
        return "BlackJack! You win!😎"
    elif user_score > 21:
        return "You bust! Dealer wins!😥"
    elif computer_score > 21:
        return "Dealer busts! You win!🤓"
    elif user_score > computer_score:
        return "You win🤪"
    else:
        return "You lose🥴"
    
def play():
    print(logo)
    user_cards = []
    computer_cards = []
    is_gameover = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_gameover:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Dealer's first card: {computer_cards[0]}") 

        if user_score == 21 or computer_score == 21 or user_score > 21:
            is_gameover = True
        else:
            action_taken = (input("Type 'y' to get another card, type 'n' to pass: "))
            if action_taken == "y":
                user_cards.append(deal_card()) 
            else:
                is_gameover = True

    while computer_score != 21 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
    print(f"    Dealer's final hand: {computer_cards} ")
    print(compare(user_score, computer_score))

def main():
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        os.system("cls")
        play()
if  __name__ == "__main__":
    main()
