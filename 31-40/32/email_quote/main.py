import datetime
import smtplib
import random


def get_random_quote():
    """Gets a random quote from quotes.txt"""
    with open("31-40/32/email_quote/quotes.txt", encoding="UTF-8") as quotes:
        quote = random.choice(quotes.readlines())
        return quote


def is_tuesday():
    """Sends a random quote if the day is tuesday"""
    now = datetime.datetime.now()
    day_of_the_week = now.weekday()
    if day_of_the_week == 1:
        return True
    return False


def send_email_with_quote(quote):
    """Sends an email with the random quote"""
    my_fake_email = "hi@gmail.com"
    fake_password = "hi_mom"
    with smtplib.SMTP("smtp.gmail.com") as connection:  # different for every provider
        connection.starttls()  # encrypts the connection
        connection.login(user=my_fake_email, password=fake_password)
        connection.sendmail(
            from_addr=my_fake_email,
            to_addrs="mom@gmail.com",
            msg=f"Subject:Tuesday Quote\n\n{quote}."  # Subject: x\n\nContent
        )


def conduct_email():
    """Conducts the email quote app"""
    tuesday = is_tuesday()
    if tuesday:
        quote = get_random_quote()
        send_email_with_quote(quote)


conduct_email()
