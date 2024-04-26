import random
# Average Height
total_height = 0
students = 0
for height in student_heights:
  total_height+= height
  students+=1
print("total height =",total_height)
print("number of students =",students)
print("average height =",round(total_height / students))

# Highest Score
student_scores = input().split()
for n in range(0, len(student_scores)):
    # does it just want n = int(student_scores[n])
    #   student_scores[n] = int(student_scores[n])
highest = student_scores[0]
for n in student_scores:
  if n > highest:
    highest = n
print(f"The highest score in the class is: {highest}")

# Adding Even Numbers
target = int(input()) # Enter a number between 0 and 1000
total_of_evens = 0
for number in range(target+1):
  if number % 2 == 0:
    total_of_evens += number
print(total_of_evens)

# Fizzbuzz
for number in range(1,101):
  if number % 5 == 0 and number % 3 == 0:
    print("FizzBuzz")
  elif number % 5 == 0:
    print("Buzz")
  elif number % 3 == 0:
    print("Fizz")
  else:
    print(number)


# Password Generator
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
           "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
           "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "<" ">"]

print("Welcome to the PyPassowrd Generator!")
letter_amount = int(input("How many letters would you like in your password?\n"))
number_amount = int(input("How many numbers would you like in your password?\n"))
symbol_amount = int(input("How many symbols would you like in your password?\n"))

password_chars = []
# could have used random.choice rather than generating a random index
# for each of these
for n in range(letter_amount):
  randidx = random.randint(0, len(letters) -1)
  password_chars.append(letters[randidx])
for n in range(number_amount):
  randidx = random.randint(0, len(numbers) -1)
  password_chars.append(numbers[randidx])
for n in range(symbol_amount):
  randidx = random.randint(0, len(symbols) -1)
  password_chars.append(symbols[randidx])
shuffled_password_chars = random.sample(password_chars, len(password_chars))
password = "".join(shuffled_password_chars)

print(f"Here is your password: {password}")