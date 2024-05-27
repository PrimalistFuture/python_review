import os
import csv
import pandas

# figuring out where we are again
# cwd = os.getcwd()  # get the current working directory
# files = os.listdir(cwd)  # get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

# with standard csv library
# with open("21-30/25/weather_data.csv", mode="r") as weather_data:
#     temps = []
#     for line in csv.reader(weather_data):
#         if line[1] != "temp":
#             temps.append(int(line[1]))
#     print(temps)

# with pandas
data = pandas.read_csv("21-30/25/weather_data.csv")

# printing a specific column
# print(data["temp"])

# Converting a data_frame to a dict
data_dict = data.to_dict()
# print(data_dict)

# Converting a series to a list
temp_list = data["temp"].to_list()
# print(temp_list)

# Using pandas to find the mean
# Notice you can't call it on the list temp_list, just the series.
temp_mean = data["temp"].mean()
# print(temp_mean)

# Using pandas to get the max
max_temp = data["temp"].max()
# print(max_temp)

# using pandas to get data in columns
# print(data["condition"])
# or
# print(data.condition)

# using pandas to get data in a row
# print(data[data.day == "Monday"])

# getting the row where we filter on a condition
# in this case the row where we get the max temp
# print(data[data.temp == data.temp.max()])

# Drilling down further and doing more
monday = data[data.day == "Monday"]
monday_temp_C = monday["temp"]
monday_temp_F = (monday_temp_C * 1.8) + 32
# print(monday_temp_F)

# Creating a Dataframe from scratch
dicto = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
pandas_dataframe = pandas.DataFrame(dicto)
# print(pandas_dataframe)

# we could then save it to a csv
pandas_dataframe.to_csv("new_data.csv")
