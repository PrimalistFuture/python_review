import pandas

# getting the data
data = pandas.read_csv(
    "21-30/25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
)

# getting the fur colors
fur_colors = data["Primary Fur Color"]
# print(fur_colors)

# Creating variables
black = 0
cinnamon = 0
gray = 0

# Populating variables with data
for color in fur_colors:
    if color == "Black":
        black += 1
    elif color == "Cinnamon":
        cinnamon += 1
    elif color == "Gray":
        gray += 1

# Creating dict
squirrel_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}

# Creating data frame
squirrel_frame = pandas.DataFrame(squirrel_dict)

# creating csv
squirrel_frame.to_csv("squirrel_colors.csv")


# __________Alternatively________
s_data = pandas.read_csv(
    "21-30/25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
)

# All data on these squirrels seperated by color
gray_squirrels = s_data[data["Primary Fur Color"] == "Gray"]
red_squirrels = s_data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = s_data[data["Primary Fur Color"] == "Black"]

# getting the count of these
gray_squirrels_amount = len(gray_squirrels)

# Then repeat the creating dict and creating data frame and creating csv steps
