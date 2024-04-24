# Instructions
# Write a program that works out whether if a given number is
# an odd or even number.

# Even numbers can be divided by 2 with no remainder.

# e.g. 86 is even because 86 ÷ 2 = 43

# 43 does not have any decimal places.
# Therefore the division is clean.

# e.g. 59 is odd because 59 ÷ 2 = 29.5

# 29.5 is not a whole number, it has decimal places.
# Therefore there is a remainder of 0.5, so the division is not clean.

# The modulo is written as a percentage sign (%) in Python.
# It gives you the remainder after a division.

# e.g.
# 6 ÷ 2 = 3 with no remainder.
# therefore: 6 % 2 = 0
# 5 ÷ 2 = 2 x 2 + 1, remainder is 1.

# Which number do you want to check?
number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


# Write a program that interprets the Body Mass Index (BMI) based on a user's
# weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Equal to or over 18.5 but below 25 they have a normal weight
# Equal to or over 25 but below 30 they are slightly overweight
# Equal to or over 30 but below 35 they are obese
# Equal to or over 35 they are clinically obese

# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = (weight / (height ** 2))
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")


# Write a program that works out whether if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in
# February.
# The reason why we have leap years is really fascinating,
# this video does it more justice.

# This is how you work out whether if a particular year is a leap year.

# on every year that is divisible by 4 with no remainder

# except every year that is evenly divisible by 100 with no remainder

# unless the year is also divisible by 400 with no remainder

# If english is not your first language or if the above logic is confusing,
# try using this flow chart .

# e.g. The year 2000:
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)

# So the year 2000 is a leap year.
# But the year 2100 is not a leap year because:

# 2100 ÷ 4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap)

# Warning your output should match the Example Output format exactly,
# including spelling an punctuation.

# Example Input 1
# 2400
# Example Output 1
# Leap year
# Example Input 2
# 1989
# Example Output 2
# Not leap year

# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 != 0:
    print("Not leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap year")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("Leap year")
else:
    print("Not leap year")


# Congratulations, you've got a job at Python Pizza!
# Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1

# Example Input
# L
# Y
# N
# Example Output
# Thank you for choosing Python Pizza Deliveries!
# Your final bill is: $28.

print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? S, M, or L
add_pepperoni = input()  # Do you want pepperoni? Y or N
extra_cheese = input()  # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
price = 0

if size == "S":
    price = 15
elif size == "M":
    price = 20
elif size == "L":
    price = 25

if add_pepperoni == "Y" and size == "S":
    price += 2
elif add_pepperoni == "Y" and (size == "M" or size == "L"):
    price += 3

if extra_cheese == "Y":
    price += 1

print(f"Your final bill is: ${price}.")


# You are going to write a program that tests the compatibility between
# two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters
# in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is *z*."
# e.g.

# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
# Total = 5

# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times
# Total = 3

# Love Score = 53
# Print: "Your score is 53."

# These functions will help you:
# lower() count()

# Example Input 1
# Kanye West
# Kim Kardashian
# Example Output 1
# The Love Calculator is calculating your score...
# Your score is 42, you are alright together.
# Example Input 2
# Brad Pitt
# Jennifer Aniston
# Example Output 2
# The Love Calculator is calculating your score...
# Your score is 73.

print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
# I made my life a lot harder here by not just combining the names immediately.
# Feels like these could be individual functions too.
name1 = name1.lower()
name2 = name2.lower()

true_count1 = 0
love_count1 = 0
true_count2 = 0
love_count2 = 0
true_total = 0
love_total = 0
total_love_and_true = 0

t_count1 = name1.count("t")
r_count1 = name1.count("r")
u_count1 = name1.count("u")
e_count1 = name1.count("e")

true_count1 = t_count1 + r_count1 + u_count1 + e_count1

t_count2 = name2.count("t")
r_count2 = name2.count("r")
u_count2 = name2.count("u")
e_count2 = name2.count("e")

true_count2 = t_count2 + r_count2 + u_count2 + e_count2

true_total = true_count1 + true_count2

love_l_count1 = name1.count("l")
love_o_count1 = name1.count("o")
love_v_count1 = name1.count("v")
love_e_count1 = name1.count("e")

love_count1 = love_l_count1 + love_o_count1 + love_v_count1 + love_e_count1

love_l_count2 = name2.count("l")
love_o_count2 = name2.count("o")
love_v_count2 = name2.count("v")
love_e_count2 = name2.count("e")

love_count2 = love_l_count2 + love_o_count2 + love_v_count2 + love_e_count2

love_total = love_count1 + love_count2

total_love_and_true = str(true_total) + str(love_total)
total_love_and_true = int(total_love_and_true)

if total_love_and_true < 10 or total_love_and_true > 90:
    print(
        f"Your score is {total_love_and_true}, you go together like coke and mentos.")
elif total_love_and_true < 50 and total_love_and_true > 40:
    print(f"Your score is {total_love_and_true}, you are alright together.")
else:
    print(f"Your score is {total_love_and_true}.")


# True Love Refactor

def letter_sum(string, chars):
    """Takes in a string and string of characters. Searches through the string for any of the input chars, and returns the total number of chars within the input string.

    str = "vaughn"
    chars = "ah"
    returns: 2
    """
    string = string.lower()
    total = 0
    for letter in range(len(string)):
        for char in range(len(chars)):
            if string[letter] == chars[char]:
                total += 1
    return total

true_total = letter_sum(name1 + name2, 'true')
love_total = letter_sum(name1 + name2, 'love')
print(str(true_total) + str(love_total))




# Treasure Island!
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
crossroads = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'.\n")
if crossroads == "left":
    lake = input("You come to a lake. There is an island in the midle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if lake == "wait":
        doors = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose?\n")
        if doors == "red":
            print("Burned by fire. Game Over.")
        elif doors == "blue":
            print("Eaten by beasts. Game Over.")
        elif doors == "yellow":
            print("You win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")

