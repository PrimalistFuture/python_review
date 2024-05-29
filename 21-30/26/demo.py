import random
import pandas

# List Comprehensions
numbers = [1, 2, 3]
new_numbers = [number + 1 for number in numbers]
# print(new_numbers)  # [2,3,4]

# with strings
name = "Vaughn"
letters = [letter for letter in name]
# print(letters)

# with range
doubled = [num * 2 for num in range(1, 5)]
# print(doubled)

# with conditional
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
# print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)


# Dictionary Comprehensions
# generic with list
# new_dict = {key: value for item in list}
# with dict
# new_dict2 = {key: value for (key, value) in dict.items()}
# conditional
# new_dict3 = {new_key: new_value for (key,value) in dict.item() if test}

# using names from above
scores = {student: random.randint(1, 100) for student in names}
# print(scores)

# with conditional
passed_students = {student: score for (
    student, score) in scores.items() if score >= 60
}
# print(passed_students)

# with input sentence
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_lengths = {word: len(word) for word in sentence.split(' ')}
# print(word_lengths)

# with starting dict
weather_c = {
    "Monday": 4,
    "Tuesday": 5,
    "Wednesday": 10,
    "Thursday": 11,
    "Friday": 12,
    "Saturday": 14,
    "Sunday": 16
}
weather_f = {day: temp_c * 1.8 + 32 for (day, temp_c) in weather_c.items()}
# print(weather_f)

# with pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
student_dataframe = pandas.DataFrame(student_dict)
# print(student_dataframe)
# looping through a dataframe rows
for (index, row) in student_dataframe.iterrows():
    # each row is a pandas Series
    print(row.student)
    if row.student == "Angela":
        print(row.score)
