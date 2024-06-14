import requests
from bs4 import BeautifulSoup
import smtplib

amz_url = "https://www.amazon.com/dp/B0CF3MVMKH/"

header = {
    "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36""",
    "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    "Accept-Language": "en-US,en;q=0.9,ko;q=0.8",
}

response = requests.get(amz_url, headers=header)

soup = BeautifulSoup(response.text, "lxml")

price_whole = soup.find(name="span", class_="a-price-whole").getText()
price_fraction = soup.find(name="span", class_="a-price-fraction").getText()
price = (price_whole + price_fraction)


def send_email():
    """Sends an email"""
    my_fake_email = "hi@gmail.com"
    fake_password = "hi_mom"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # encrypts the connection
        connection.login(user=my_fake_email, password=fake_password)
        connection.sendmail(
            from_addr=my_fake_email,
            to_addrs=my_fake_email,
            msg=f"Low Price for Amazon Product\n\n{
                amz_url}"  # Subject: x\n\nContent
        )


target_price = 55
if price < target_price:
    send_email()
