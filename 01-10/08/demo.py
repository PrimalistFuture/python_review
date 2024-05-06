import math
# Paint Can Calculator
# One can of paint can cover 5 square meteres of wall. Given a random height and width of a wall, calc  how many cans of paint you'll need to buy.
# number of cans = (height * width) / coverage per can
test_h = int(input())
test_w = int(input())
coverage = 5

def paint_calc(height, width, cover):
    cans = (height * width) / cover
    round_up_cans = math.ceil(cans)
    print(f"You'll need {round_up_cans} cans of paint.")

paint_calc(height=test_h, width=test_w, cover=coverage)


# Prime number calc
# checks if an input num is a prime number
n = int(input())

def prime_checker(n):
    comparison = n - 1
    while comparison > 1:
        if n % comparison == 0:
            return True
        else:
            comparison -= 1
    return False        

# Their solution
# def prime_checker(number):
#   is_prime = True
#   for i in range(2, number):
#       if number % i == 0:
#           is_prime = False
#       if is_prime:
#           print("It's a prime number.")
#       else:
#           print("It's not a prime number.")


prime_checker(number=n)


# Ceaser Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

from art import logo
print(logo)

should_end = False
while not should_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")
