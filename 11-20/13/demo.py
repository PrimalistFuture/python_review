# debugging

# whats the bug?
def range_function():
    for i in range(1, 20):  # range counts up to, but not including the second parameter
        if i == 20:
            print("You got it")
range_function()

# whats the bug?
from random import randint
dice_imgs = ["1", "2", "3", "4", "5", "6"] 
dice_num = randint(1,6)  
print(dice_imgs[dice_num]) # will error out if dice_num evaluates to 6, but 'work' everyother time. This is because dice_imgs[6] is out of range. Worth noting we will never get the "1" from dice_imgs either.

# whats the bug? what happens if the input is 1994?
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:  # should be year <= 1994
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")

# whats the bug?
age = input("How old are you? ") # what does input always return?
if age > 18:
print("You can drive at age {age}")  # The editor is telling us that it thinks the print should be indented. But there is another bug too

# whats the bug?
pages = 0
words_per_page = 0
pages = int(input("Number of pages: "))
words_per_page == int(input("Number of words per page: ")) # whats the diff between = and ==
total_words = pages * words_per_page
print(total_words)


# whats the bug?
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item) # what is new_item when this line runs?
    print(b_list)
mutate([1,2,3,5,8,13])  # [26]