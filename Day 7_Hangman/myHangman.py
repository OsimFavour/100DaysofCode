import random
from hangman_words import word_list
from hangman_art import logo, stages


def hangman():
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    end_game = False
    lives = len(stages) - 1
    print(logo)
    display = []
    for _ in range(word_length):
        display += "_" 
    while not end_game:
        guess = input("\nGuess a letter: ") 
        if guess in display:
            print(f"You've already guessed letter {guess}")
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter  
        if guess not in chosen_word:
            print(f"{guess} is not in word")
            lives -= 1
            if lives == 0:
                end_game = True
                print("You lose")
                print(f"The word was {chosen_word}")
        print("".join(display))
        if "_" not in display:
            end_game = True
            print("You win")   
        print(stages[lives])
hangman()
       
def main():
    while input("Play Again? (y/n) ").lower() == "y":
        hangman()
if  __name__ == "__main__":
    main()
    


