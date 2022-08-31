import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
nato_alphabet = {row.letter: row.code for (index, row) in alphabet.iterrows()}
# print(nato_alphabet)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word_input = input("Enter a Word: ").upper()
output = [nato_alphabet[letter] for letter in word_input]
print(output)
