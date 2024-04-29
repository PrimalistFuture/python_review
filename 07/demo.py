import random

MAX_GUESSES = 6
EIGHT_LETTER_WORDS = ["absolute", "sentence", "mountain", "children", "bacteria",
                      "dramatic", "educated", "firewall", "fraction", "homeless",
                      "informed", "likewise", "opponent", "pleasant", "religion",
                      "required", "tropical", "unlikely" , "valuable", "warranty",
                      "yourself"]

target_word = random.choice(EIGHT_LETTER_WORDS)

censored_word = target_word
for char in censored_word:
    char = "_"

print("Welcome to Hangman!")
print(censored_word)
while MAX_GUESSES > 0:
    letter = input("What letter would you like to guess?")
    if letter not in target_word:
        MAX_GUESSES -= 1
        print(f"The letter {letter} is not in the word. You have {MAX_GUESSES} remaining.")
    else:
        indices = [i for i, char in enumerate(target_word) if char == letter]
        for char in range(len(censored_word)):
            if char in indices:
                char = letter
        print(f"{letter} was in the word. You have {MAX_GUESSES} remaining.")
print("The man has been hanged. Game over.")