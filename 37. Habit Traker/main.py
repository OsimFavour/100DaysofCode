# This was the function I used to test the multiple tracker class in one code
# by writing a complete all round code for the 'code tracker' first

import requests
from datetime import datetime

USERNAME = "osimfavour"
TOKEN = "hb74ue2jedkcjdakmswp0p02d"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Get Graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "code tracker",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# current day
today = datetime.now()


def make_commits():
    """Post a Pixel"""
    pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    pixel_data = {
        "date": today.strftime("%Y%m%d"),
        "quantity": input("How many hours did you code today? ")
    }

    response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
    if "Success" in response.text:
        print(f"{response.text}\nsuccess in commit")
    else:
        print(response.text)


def update_today():
    """Update a Pixel"""
    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
    pixel_update = {
        "quantity": input("How many hours did you code today? ")
    }

    response = requests.put(url=update_endpoint, json=pixel_update, headers=headers)
    if "Success" in response.text:
        print(f"{response.text}\nToday's commit updated")
    else:
        print(response.text)


def delete_today():
    """Delete a Pixel"""
    delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

    response = requests.delete(url=delete_endpoint, headers=headers)
    if "Success" in response.text:
        print(f"{response.text}\nToday's commit deleted successfully")
    else:
        print(response.text)


def update_other_day():
    """Update a Pixel for some other day"""
    year = int(input("Input Year: "))
    month = int(input("Input Month: "))
    day = int(input("Input Day: "))
    date_to_update = datetime(year=year, month=month, day=day)
    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_update.strftime('%Y%m%d')}"
    pixel_update = {
        "quantity": input("How many hours was it? ")
    }

    response = requests.put(url=update_endpoint, json=pixel_update, headers=headers)
    if "Success" in response.text:
        print(f"{response.text}\nUpdated Successfully")
    else:
        print(response.text)


def delete_other_day():
    """Delete a Pixel for some other day"""
    year = int(input("Input Year: "))
    month = int(input("Input Month: "))
    day = int(input("Input Day: "))
    date_to_delete = datetime(year=year, month=month, day=day)
    delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_delete.strftime('%Y%m%d')}"

    response = requests.delete(url=delete_endpoint, headers=headers)
    if "Success" in response.text:
        print(f"{response.text}\nDeleted Successfully")
    else:
        print(response.text)


question = input("Do you want to MAKE, CHANGE, or DELETE a commit? ")
if "MAKE".lower() in question:
    make_commits()
elif "CHANGE".lower() in question:
    update_question = input("Change for CURRENT DAY or DAY IN THE PAST? ")
    if "CURRENT".lower() in update_question:
        update_today()
    elif "PAST".lower() or "BEFORE".lower() in update_question:
        update_other_day()
elif "DELETE".lower() in question:
    delete_question = input("Delete for CURRENT DAY or DAY IN THE PAST? ")
    if "CURRENT".lower() in delete_question:
        delete_today()
    elif "PAST".lower() or "BEFORE".lower() in delete_question:
        delete_other_day()
else:
    print("Typo Error!")
