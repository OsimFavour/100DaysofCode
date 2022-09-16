import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
phone_number = os.environ.get("PHONE_NUMBER")

parameters = {
    "lat": 9.061460,
    "lon": 7.500640,
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status
data = response.json()

weather = data["weather"][0]["id"]

if weather < 700:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain, Remember to bring an ☔",
            from_="+17076753490",
            to=phone_number
        )

print(message.status)  
