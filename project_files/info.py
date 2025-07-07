origin = input("Enter origin IATA code (e.g., LON, JFK): ").strip().upper()

departure_date = input("Enter departure date (YYYY-MM-DD) or type 'use' to use today's date: ").strip().lower()
if not departure_date:
    departure_date = 'use'

while True:
    try:
        adults = int(input("Enter number of adult passengers: ").strip())
        if adults >= 0:
            break
        else:
            print("Number must be 0 or more.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    try:
        children = int(input("Enter number of child passengers: ").strip())
        if children >= 0:
            break
        else:
            print("Number must be 0 or more.")
    except ValueError:
        print("Please enter a valid number.")

currency = input("Enter currency code (e.g., USD, EUR): ").strip().upper()

valid_classes = ['E', 'P', 'B', 'F']
while True:
    travel_class = input("Choose travel class (E = Economy, P = Premium, B = Business, F = First): ").strip().upper()
    if travel_class in valid_classes:
        break
    else:
        print("Invalid class. Please choose E, P, B, or F.")
