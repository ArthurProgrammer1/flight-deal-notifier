import os
import requests


class DataManager:
    def __init__(self):
        self.sheety_endpoint = os.getenv("SHEETY_ENDPOINT")

    def get_sheety_info(self):
        response = requests.get(url=f'{self.sheety_endpoint}/prices')
        response.raise_for_status()
        response_data = response.json()

        return [(item['city'], item['lowestPrice']) for item in response_data['prices']]
