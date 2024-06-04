import datetime
import smtplib

# SMTP PATTERN
my_fake_email = "hi@gmail.com"
fake_password = "hi_mom"
with smtplib.SMTP("smtp.gmail.com") as connection:  # different for every provider
    connection.starttls()  # encrypts the connection
    connection.login(user=my_fake_email, password=fake_password)
    connection.sendmail(
        from_addr=my_fake_email,
        to_addrs="mom@gmail.com",
        msg="Subject:Hi Mom\n\nThis is the body of the email."  # Subject: x\n\nContent
    )


now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
day_of_the_week = now.weekday()


# hour and so on can be set, but not mandatory
date_of_birth = datetime.datetime(year=1989, month=10, day=15)
print(date_of_birth)
