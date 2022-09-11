import requests
from datetime import datetime
import smtplib
import time
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

MY_LAT = 51.507351    
MY_LONG = -0.127758    

def is_iss_overhead():
    """checking whether if the iss position is at a similar position to my position"""
    response =requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print(data)

    iss_latitude = data["iss_position"]["latitude"]
    iss_longitude = data["iss_position"]["longitude"]

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    print(data)
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    print(sunrise)
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunset)
    time_now = datetime.now().hour

    print(time_now)

    if time_now >= sunset or time_now <= sunrise:
        # that means it's dark
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="famos204@gmmail.com",
            msg="Suubject:Look Up👆\n\nThe ISS is above you in the sky."
        )


