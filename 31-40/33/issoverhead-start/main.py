from datetime import datetime
import smtplib
import requests

MY_LAT = 37.774929  # Your latitude
MY_LONG = -122.419418  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


def iss_within_five_degrees():
    """Returns true if my lat and long are within 5 degrees of the ISS. False otherwise"""
    return (abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5)


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "tzid": "America/Los_Angeles",
    "formatted": 0,
}

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print("sun sets", sunset)
time_now = datetime.now()
print("now", time_now.hour)


def is_dark():
    """Checks sunset and sunrise time to return True if it is dark"""
    return (sunset < time_now.hour or time_now.hour <= sunrise)

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


def send_email_with_quote():
    """Sends an email"""
    my_fake_email = "hi@gmail.com"
    fake_password = "hi_mom"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # encrypts the connection
        connection.login(user=my_fake_email, password=fake_password)
        connection.sendmail(
            from_addr=my_fake_email,
            to_addrs=my_fake_email,
            msg="Subject:ISS Overhead\n\nLook up!."  # Subject: x\n\nContent
        )


def iss_overhead_conductor():
    """Conductor"""
    if is_dark() and iss_within_five_degrees():
        send_email_with_quote()
