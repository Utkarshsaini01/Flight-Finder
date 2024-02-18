import requests
import os

BEARER = os.environ.get("BEARER")
# sheety username
USERNAME = os.environ.get("USERNAME")

PROJECT = os.environ.get("PROJECT_NAME")
SHEET = os.environ.get("SHEET_NAME")

base_url = "https://api.sheety.co"


def post_new_row(first_name, last_name, email):
    endpoint_url = f"/{USERNAME}/{PROJECT}/{SHEET}"
    url = base_url + endpoint_url

    headers = {
        "Authorization": f"Bearer {BEARER}",
        "Content-Type": "application/json"
    }

    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }

    response = requests.post(url=url, headers=headers, json=body)
    response.raise_for_status()
    print(response.text)


