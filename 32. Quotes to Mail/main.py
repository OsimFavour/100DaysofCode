import datetime as dt
import random
import smtplib
import os

EMAIL_ADDRESS = os.environ.get('MY_EMAIL')
EMAIL_PASSWORD = os.environ.get('MY_PASSWORD')

now = dt.datetime.now()

if now.weekday() == 4:

    with open("quotes.txt", "r", encoding="utf8") as files:
        file = files.read().splitlines()
        any_file = random.choice(file)

        subject = "Morning quotes"
        body = any_file

        message = f"Subject: {subject}\n\n{body}"

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=EMAIL_ADDRESS,
                to_addrs="famos204@gmail.com",
                msg=message.encode("utf-8"))

