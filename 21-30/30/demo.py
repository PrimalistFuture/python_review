# Errors

# This is a filenotfound error and will result in a crash
with open("a_file.txt") as file:
    file.read()

# Key error
a_dictionary = {"key": "value"}
value = a_dictionary["non_existent_key"]

# IndexError
fruit_list = ["Apple", "Banana", "Pear"]
fruit = fruit_list[3]

# TypeError
text = "abc"
print(text + 5)

# With error handling
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
except FileNotFoundError:
    open("a_file.txt", "w")  # will create this file
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:  # only runs if there are no caught errors
    content = file.read()
    print(content)
finally:  # runs regardless
    file.close()

# with raise
# won't result in an error, but it probably should in some cases
height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
