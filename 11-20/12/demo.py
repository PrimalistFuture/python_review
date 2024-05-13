# Scope 

enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()   # prints 2
print(f"enemies outside function {enemies}")  # prints 1

# Local Scope
enemies = 1

def decrease_enemies():
    # enemies = 1  without this line, this throws an error
    enemies -= 1
    print(f"enemies inside function: {enemies}")

decrease_enemies()  # prints an error, because it thinks enemies inside has not yet been defined
print(f"enemies outside function {enemies}")  # prints 1



# Number Guessing Game
import random

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def check_answer(guess, answer, attempts):
    """Checks answer against guess, returns number of attempts remaining"""
    if guess > answer:
        print("Too high.")
        return attempts -1
    elif guess < answer:
        print("Too low.")
        return attempts -1
    elif guess == answer:
        print(f"You got it! The answer was {answer}")
        return
    

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_ATTEMPTS
    else: 
        return HARD_ATTEMPTS
def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1,100)

    attempts = set_difficulty()
    
    guess = -1
    while guess is not answer:
        print(f"You have {attempts} attempts remaining.")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, answer, attempts)
        if attempts == 0:
            print("You've run out of attempts, you lose.")
            return

game()