# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Round the result to 2 decimal palces = 33.60


print("Welcome to the tip calculator!")

bill = float(input("What was the total bill?\n$"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))

people = int(input("How many people to split the bill?\n"))

# Using the formula of BODMAS
new_bill = tip / 100 * bill + bill 

number_of_people = new_bill / people
number_of_people = round(number_of_people, 2)

print(f"Each person should pay the bill: ${number_of_people}")