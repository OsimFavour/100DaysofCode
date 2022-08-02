import higher_lower
import random
from game_data import data

# A new algorithm I discovered, to make the 
# second guess replace the first guess if guessed correct 

account_b = random.choice(data)
account_a = account_b
account_b = random.choice(data)