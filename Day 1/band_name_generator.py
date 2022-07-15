"""Write a band name generator that asks you for the city you
   grew up in, asks for the name of your pet and then combines
   them together to give you the name of your band
"""

print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")

band_name = city + " " + pet

print("Your band name could be", band_name)