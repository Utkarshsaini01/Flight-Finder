import requests
import os

from pprint import pprint

SHEETY_API_TOKEN = os.environ.get("SHEETY_API_TOKEN")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEET_USERS_ENDPOINT = os.environ.get("SHEET_USER_ENDPOINT")


header = {
    "Authorization": SHEETY_API_TOKEN
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.customer_data = []

    def get_destination_data(self):
        response = requests.get(SHEETY_ENDPOINT, headers=header).json()
        self.destination_data = response['prices']
        # pprint(response)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data, headers=header)
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEET_USERS_ENDPOINT
        response = requests.get(customers_endpoint, headers=header)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data