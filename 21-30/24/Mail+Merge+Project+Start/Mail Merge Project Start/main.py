import os

# cwd = os.getcwd()  # get the current working directory
# files = os.listdir(cwd)  # get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


def open_and_strip_names():
    """Opens the file with the names"""
    striped_names = []
    with open("""21-30/24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt""", mode="r") as names:
        for name in names.readlines():
            name = name.strip("\n")
            striped_names.append(name)
        return striped_names


def create_letter_with_name_replaced(name):
    """Replaces placeholder [name] with input name"""
    with open(f"""21-30/24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter_{name}.txt""", mode="w") as letter:
        starting_letter = copy_starting_letter()
        for line in starting_letter:
            letter.write(line.replace("[name]", name))


def copy_starting_letter():
    """Copys the lines of the starting letter"""
    with open(f"""21-30/24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt""", mode="r") as starting_letter:
        return starting_letter.readlines()


def conductor():
    """Conducts the letter creation"""
    names_list = open_and_strip_names()
    for name in names_list:
        create_letter_with_name_replaced(name)


# names = open_names()
# print(names)
# create_letter_with_name_replaced('hi')
# copy_starting_letter()
conductor()
