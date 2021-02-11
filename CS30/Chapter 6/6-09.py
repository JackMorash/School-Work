favorite_places = {
    'jack': ['cologne', 'vancouver', 'london'],
    'arden': ['phoenix', 'vancouver'],
    'chris': ['china', 'red square', 'forbidden palace']
    }

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")