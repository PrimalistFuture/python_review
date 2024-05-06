import random
# between and including 1-10
random_integer = random.randint(1,10)
# float between 0-1
random_float = random.random()
# float between 0-5
random_float * 5

# Lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# nested list
dirty_dozen = [fruits, vegetables]







# Heads or Tails
rand_int = random.randint(0,1)
if rand_int == 1:
    print("Heads")
else:
    print("Tails")

# Bill Pay Randomizer
names = names_string.split(", ")
payer_idx = random.randint(0, len(names)-1)
print(f"{names[payer_idx]} is going to buy the meal today!")

# Treasure Hunt
line1 = [" "," "," "]
line2 = [" "," "," "]
line3 = [" "," "," "]
map = [line1, line2, line3]
position = input()
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

# Rock Paper Scissors
player_choice_idx = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

rps = ["Rock", "Paper", "Scissors"]
player_choice = rps[player_choice_idx]
computer_choice = rps[random.randint(0,2)]

if player_choice == computer_choice:
    print(f"You choose {player_choice} and the computer choose {computer_choice}. Draw.")
elif player_choice == "Rock" and computer_choice == "Paper":
    print(f"You choose {player_choice} and the computer choose {computer_choice}. The Computer Wins!")
elif player_choice == "Rock" and computer_choice == "Scissors":
    print(f"You choose {player_choice} and the computer choose {computer_choice}. You win!")
elif player_choice == "Paper" and computer_choice == "Rock":
    print(f"You choose {player_choice} and the computer choose {computer_choice}. You win!")
elif player_choice == "Paper" and computer_choice == "Scissors":
    print(f"You choose {player_choice} and the computer choose {computer_choice}. The Computer Wins!")
elif player_choice == "Scissors" and computer_choice == "Paper":
    print(f"You choose {player_choice} and the computer choose {computer_choice}. You win!")
elif player_choice == "Scissors" and computer_choice == "Rock":
    print(f"You choose {player_choice} and the computer choose {computer_choice}. The Computer Wins!")
