import pandas

# TODO 1. Create a dictionary of letters and nato codes from csv
nato_data = pandas.read_csv(
    "21-30/26/NATO-alphabet-start/nato_phonetic_alphabet.csv"
)
nato_dataframe = pandas.DataFrame(nato_data)

nato_alpha = {
    row.letter: row.code for (index, row) in nato_dataframe.iterrows()
}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter a word: \n").upper()
natod = [nato_alpha[letter] for letter in name]
print(natod)
