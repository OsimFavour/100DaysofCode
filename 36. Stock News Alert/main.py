import requests
from twilio.rest import Client
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "STZABVRD3Y3TQKNQ"
NEWS_API_KEY = "74935088be024514beb86c918fcb49d0"
TWILIO_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN =  os.environ.get("TWILIO_AUTH_TOKEN")

stock_parameters = {
    "function": "TIME_SERIES_DAILY", 
    "symbol": STOCK_NAME, 
    "apikey": STOCK_API_KEY
    }

response = requests.get(STOCK_ENDPOINT, stock_parameters)
response.raise_for_status()
response_json = response.json()
data = response_json["Time Series (Daily)"]

new_data = [value for (key, value) in data.items()]  
yesterday_price = new_data[0]
yesterday_closing_price = yesterday_price["4. close"]

day_before_yesterday_price = new_data[1]
day_before_yesterday_closing_price = day_before_yesterday_price["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
up_down = None
if difference > 5:
    up_down = "🔼"
else:
    up_down = "🔽"
diff_percent = round((difference / float(yesterday_closing_price)) * 100)

if diff_percent > 5:
    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
        }

    NEWS_ENDPOINT = "https://newsapi.org/v2/everything?"

    news_response = requests.get(NEWS_ENDPOINT, news_parameters)
    news_response_json = news_response.json()["articles"][:3]

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}\nBrief: {article['description']}" for article in news_response_json]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+17076753490",
            to="+2348130039337"
        )

    print(message.status)
