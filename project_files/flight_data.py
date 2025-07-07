from data_manager import DataManager
from flight_search import FlightSearch
from info import origin, departure_date, adults, children, currency, travel_class
from datetime import datetime

class FlightData:
    def __init__(self):
        self.dm = DataManager()
        self.fs = FlightSearch()
        self.sheety_data = self.dm.get_sheety_info()
        self.IATA_codes = {
            'Paris': 'CDG',
            'Frankfurt': 'FRA',
            'Tokyo': 'HND',
            'Hong Kong': 'HKG',
            'Istanbul': 'IST',
            'Kuala Lumpur': 'KUL',
            'New York': 'JFK',
            'San Francisco': 'SFO',
            'Dublin': 'DUB',
            'Edinburgh': 'EDI'
        }

    def check_prices(self):
        travel_class_dict = {
            'E': 'ECONOMY',
            'P': 'PREMIUM_ECONOMY',
            'B': 'BUSINESS',
            'F': 'FIRST'
        }

        class_code = travel_class[0].upper()
        chosen_class = travel_class_dict.get(class_code, 'ECONOMY')
        departure = datetime.today().strftime('%Y-%m-%d') if departure_date == 'use' else departure_date

        for city, max_price in self.sheety_data:
            dest_code = self.IATA_codes.get(city)
            if not dest_code:
                print(f"No IATA code found for {city}")
                continue

            price, price_currency = self.fs.get_amadeus_info(
                origin=origin,
                destination=dest_code,
                departure_date=departure,
                adults=adults,
                children=children,
                travel_class=chosen_class,
                currency=currency
            )

            if price is None:
                print(f"No offers found for {city}.")
                continue

            if float(price) <= float(max_price):
                print(f"\nCHEAP FLIGHT ALERT ✈️\n{origin} --> {dest_code} ({city})\nOnly: {round(float(price), 2)} {price_currency}\n")
            else:
                print(f"Too expensive to fly to {city} now.")
