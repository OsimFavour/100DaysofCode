print('''

              {}           {}
                \  _---_  /
                 \/     \/
                  |() ()|
                   \ + /
                  / HHH  \\
                 /  \_/   \\
               {}          {} 

 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                               



*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* 
''')


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
cross_road = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n ')
cross_road = cross_road.lower()
if cross_road == "left":
    next_move = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across\n ')
    next_move = next_move.lower()
    if next_move == "wait":
        house_doors = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose.\n ")
        house_doors = house_doors.lower()
        if house_doors == "yellow":
            print("You find the treasure. You Win!")
        elif house_doors == "red":
            print("It's a room full of fire. Game Over.")
        elif house_doors == "blue":
            print("That's a room full of beasts. Game Over")
        else:
                    print("You chose a door that doeesn't exist")
    elif next_move == "swim":
        print("There is a crocodile inside the water, why can't you just wait for a boat")
    else:
        print('Wrong keyword. Type either "swim" or "wait"')
elif cross_road == "right":
    print("There is no road there my dear. Game Over")
else:
    print('Wrong Keyword. Type either "right" or "left"')