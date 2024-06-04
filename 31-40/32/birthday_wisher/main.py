import smtplib
import datetime
import pandas
import random


##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
# Done
# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

############# Constants      ##########################
MY_FAKE_EMAILL = "hi@gmail.com"
FAKE_PASSWORD = "hi_mom"

#############################################################


def check_for_birthday():
    """Gets the current datetime and checks birthday.csv with pandas for match
    Returns the name and email if match"""

    now = datetime.datetime.now()  # gets the current datetime
    day = now.day  # gets the current day
    month = now.month  # gets the current month

    birthdays_csv = pandas.read_csv("31-40/32/birthday_wisher/birthdays.csv")

    birthdays = pandas.DataFrame.to_dict(
        birthdays_csv,
        orient="records"  # changes the shape of the data to be a list of dicts
    )

    for birthday in birthdays:
        if day == birthday["day"] and month == birthday["month"]:
            # If there are multiple birthdays, it will only get the first
            # definitely fixable
            # could return a list of birthdays, then iterate through them in the conductor?
            return {
                "name": birthday["name"],
                "email": birthday["email"]
            }


def get_random_letter():
    """Uses random to return a random letter"""
    letter_num = random.randint(1, 3)
    # with open(f"31-40/32/birthday_wisher/letter_templates/letter_{letter_num}.txt") as letter:
    return copy_starting_letter(letter_num)


def copy_starting_letter(num):
    """Copys the lines of the starting letter"""
    with open(
        f"31-40/32/birthday_wisher/letter_templates/letter_{num}.txt", mode="r",
        encoding="UTF-8"
    ) as starting_letter:
        return starting_letter.readlines()


def replace_name_in_letter(letter, name):
    """Replaces placeholder [NAME] with input name"""
    new_letter = ""
    for line in letter:
        new_letter = new_letter + line.replace("[NAME]", name)

    return new_letter


def send_email_with_letter(recipient_email, birthday_letter):
    """Sends input birthday letter to input email"""

    with smtplib.SMTP("smtp.gmail.com") as connection:  # different for every provider
        connection.starttls()  # encrypts the connection
        connection.login(user=MY_FAKE_EMAILL, password=FAKE_PASSWORD)
        connection.sendmail(
            from_addr=MY_FAKE_EMAILL,
            to_addrs=recipient_email,
            msg=f"Subject:Happy Birthday\n\n{
                birthday_letter}."  # Subject: x\n\nContent
        )


def conduct_birthday_emails():
    """Conducts the birthday email app"""
    birthday_target = check_for_birthday()
    if birthday_target:
        starting_letter = get_random_letter()
        personalized_letter = replace_name_in_letter(
            starting_letter,
            birthday_target["name"]
        )
        send_email_with_letter(birthday_target["email"], personalized_letter)


conduct_birthday_emails()
