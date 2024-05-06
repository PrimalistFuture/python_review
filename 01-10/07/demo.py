import random

# My HangMan Solution
MAX_GUESSES = 6
EIGHT_LETTER_WORDS = ["absolute", "sentence", "mountain", "children", "bacteria",
                      "dramatic", "educated", "firewall", "fraction", "homeless",
                      "informed", "likewise", "opponent", "pleasant", "religion",
                      "required", "tropical", "unlikely" , "valuable", "warranty",
                      "yourself"]

target_word = random.choice(EIGHT_LETTER_WORDS)

censored_word = []
for char in target_word:
    censored_word += "_"

print("Welcome to Hangman!")
print(censored_word)
while MAX_GUESSES > 0:
    letter = input("What letter would you like to guess?")
    letter = letter.lower()
    if letter not in target_word:
        MAX_GUESSES -= 1
        print(f"The letter {letter} is not in the word. You have {MAX_GUESSES} remaining.")
    else:
        indices = [i for i, char in enumerate(target_word) if char == letter]
        for idx, letter in enumerate(target_word):
            if idx in indices:
                censored_word[idx] = letter
        if "".join(censored_word) == target_word:
            print("You saved the hanged man! Game over.")
        print(f"{letter} was in the word. You have {MAX_GUESSES} remaining.")
print("The man has been hanged. Game over.")


# Their HangMan walkthrough
#Step 5

import random
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo
print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
        
    from hangman_art import stages
    print(stages[lives])