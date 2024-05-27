import os

# The below revealed that I am I was not 'deep' enough for the open() to work
# cwd = os.getcwd()  # get the current working directory
# files = os.listdir(cwd)  # get all the files in that directory
# print("Files in %r: %s" % (cwd, files))


# opening a file
file = open("21-30/24/my_file.txt")
contents = file.read()
print(contents)
file.close()

# another way of opening a file. Doesn't need to be closed
with open("21-30/24/my_file.txt") as file:
    contents = file.read()
    print(contents)

# write to a file
# notice the mode
# "w" will overwrite
# "a" will append
with open("21-30/24/my_file.txt", mode="a") as file:
    file.write("\nNew text.")
    print(file)

# if the file doesn't exist, it will create it for us
with open("21-30/24/new_file.txt", mode="w") as file:
    file.write("\nNew text.")
    print(file)


# high score
player_high_score = 4
with open("21-30/24/data.txt") as data:
    current_high_score = int(data.read())

    if current_high_score < player_high_score:
        with open("21-30/24/data.txt", mode="w") as data:
            data.write(f"{player_high_score}")


#  readlines() puts the data into an array
with open("21-30/25/weather_data.csv", mode="r") as weather_data:
    print(weather_data.readlines())
