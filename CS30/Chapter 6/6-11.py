cities = {
    'regina': {
        'country': 'canada',
        'population': 228_928,
        'fact': 'it is super flat',
        },
    'toronto': {
        'country': 'canada',
        'population': 2_930_000,
        'fact': 'it has the CN tower',
        },
    'berlin': {
        'country': 'germany',
        'population': 3_645_000,
        'fact': 'it has the brandenburg gate',
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact'].title()

    print(f"\n{city.title()} is in {country}.")
    print(f"  It has a population of about {population}.")
    print(f"{fact}")