import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

is_wrong = True

while is_wrong:
    word = input("enter you name: ").upper()
    try:
        list_name = [dict[letter] for letter in word]
    except KeyError:
        print("only letters please")
    else:
        is_wrong = False

print(list_name)
