def city_country(city, country):
    return f"{city.title()}, {country.title()}"

city = city_country('regina', 'canada')
print(city)

city = city_country('frankfurt', 'germany')
print(city)

city = city_country('izmir', 'turkey')
print(city)