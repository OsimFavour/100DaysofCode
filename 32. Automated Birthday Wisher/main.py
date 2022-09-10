import datetime as dt
import random
import pandas
import smtplib
import os
from email.message import EmailMessage

MY_EMAIL_ADDRESS = os.environ.get("MY_EMAIL")
EMAIL_PASSWORD = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
day = now.day
month = now.month
today = (month, day)

birthday = pandas.read_csv("birthdays.csv")
birthdays_dict = {(birth["month"], birth["day"]): birth for (index, birth) in birthday.iterrows()}

if today in birthdays_dict:
	celebrant = birthdays_dict[today]
	# pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates
	with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file_path:
		write_up = file_path.read()
		write_up = write_up.replace("[NAME]", celebrant["name"])

	with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
		connection.login(MY_EMAIL_ADDRESS, EMAIL_PASSWORD)

		msg = EmailMessage()
		msg["Subject"] = "Happy Birthday!"
		msg["From"] = MY_EMAIL_ADDRESS
		msg["To"] = celebrant["email"]
		msg.set_content(write_up)

		connection.send_message(msg)
