import os
import requests

class FlightSearch:
    def __init__(self):
        self.amadeus_endpoint = 'https://test.api.amadeus.com'
        self.client_id = os.getenv("AMADEUS_CLIENT_ID")
        self.client_secret = os.getenv("AMADEUS_CLIENT_SECRET")

    def post_token(self):
        token_data = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        response = requests.post(f'{self.amadeus_endpoint}/v1/security/oauth2/token', data=token_data)
        response.raise_for_status()
        return response.json()['access_token']

    def get_amadeus_info(self, origin, destination, departure_date, adults, children, travel_class, currency, max=5):
        try:
            token = self.post_token()
            headers = {'Authorization': f'Bearer {token}'}
            params = {
                'originLocationCode': origin,
                'destinationLocationCode': destination,
                'departureDate': departure_date,
                'adults': adults,
                'children': children,
                'travelClass': travel_class,
                'currencyCode': currency,
                'max': max
            }

            response = requests.get(f'{self.amadeus_endpoint}/v2/shopping/flight-offers', params=params, headers=headers)
            response.raise_for_status()
            data = response.json()

            if not data.get('data'):
                return None, None

            offer = data['data'][0]['price']
            return offer['total'], offer['currency']

        except Exception as e:
            print(f"Error fetching Amadeus data: {e}")
            return None, None
