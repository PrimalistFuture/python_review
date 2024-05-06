# tip calculator

# greeting
print("Welcome to the tip calculator!")
# input for total
total = float(input("What was the total bill?"))
# tip percentage
tip_percentage = input("How much tip would you like to give? 10, 12, or 15?")
tip_percentage = (int(tip_percentage) / 100) + 1
# people to split bill with?
people = int(input("How many people to split the bill?"))
# calculation
per_person_total = round((total * tip_percentage) / people, 2)
print(f'Each person should pay ${per_person_total}')


# Auditorium tasks

# 1
# Instructions
# Write a program that adds the digits in a 2 digit number.
# e.g. if the input was 35, then the output should be 3 + 5 = 8
# Warning. Do not change the code on line 1.
# Your program should work for different inputs. e.g. any two-digit number.
# The last line of your program should print the result.

two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
str1 = str(two_digit_number)
first_number = int(str1[0])
second_number = int(str1[1])
print(first_number + second_number)

# 2
#  instructions
# Write a program that calculates the Body Mass Index (BMI)
# from a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height.
# e.g. If a tall person and a short person both weigh the same amount,
# the short person is usually more overweight.

# The BMI is calculated by dividing a
# person's weight (in kg) by the square of their height (in m):
# NOTE:  You should convert the bmi to a whole number

# and print out a whole number in order to pass all the tests.
# See examples below.
# Example Input 1
# 1.75
# 80
# means: weight = 80 and height = 1.75

# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height = float(height)
weight = float(weight)
bmi = int(weight / (height * height))
print(bmi)


# # Instructions
# # I was reading this article by Tim Urban - Your Life in Weeks and
# realised just how little time we actually have.

# # Create a program using maths and f-Strings that tells us
# how many weeks we have left, if we live until 90 years old.

# # It will take your current age as the input and output a
# message with our time left in this format:

# # You have x weeks left.
# # Where x is replaced with the actual calculated number of weeks
# the input age has left until age 90.

# # Warning your output should match the
# Example Output format exactly, even the positions of the commas and full
# stops.

# # Example Input
# # 56
# # Example Output
# # You have 1768 weeks left.

age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
expected_years = 90
weeks_in_a_year = 52
lifetime_weeks = expected_years * weeks_in_a_year

age = int(age)
input_age_in_weeks = age * weeks_in_a_year

weeks_remaining = lifetime_weeks - input_age_in_weeks
print(f'You have {weeks_remaining} weeks left.')
