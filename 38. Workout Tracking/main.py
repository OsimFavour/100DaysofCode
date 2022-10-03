import requests
from datetime import datetime
import os

N_APP_ID = os.environ.get("N_APP_ID")
N_API_KEY = os.environ.get("N_API_KEY")

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("Tell me which exercises you did: ")

user_params = {
 "query": query,
 "gender": "male",
 "weight_kg": 72.5,
 "height_cm": 167.64,
 "age": 22
}

headers = {
    "x-app-id": N_APP_ID,
    "x-app-key": N_API_KEY
}
response = requests.post(nutrition_endpoint, json=user_params, headers=headers)
response_json = response.json()

current_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%X")


sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")

bearer_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

for exercise in response_json["exercises"]:

    sheety_info =  {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    
    sheety_response = requests.post(sheety_endpoint, json=sheety_info, headers=bearer_headers)
    print(sheety_response.text)
