# Make an empty list to store people in.
people = []

# Defines and adds people to the "people" list
person = {
    'first_name': 'jack',
    'last_name': 'morash',
    'age': 17,
    'city': 'regina',
    }
people.append(person)

person = {
    'first_name': 'arden',
    'last_name': 'sinclair',
    'age': 18,
    'city': 'regina',
    }
people.append(person)

person = {
    'first_name': 'ali',
    'last_name': 'nossier',
    'age': 16,
    'city': 'regina',
    }
people.append(person)

# Display all of the information in the dictionary.
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()

    print(f"{name}, from {city}, is {age} years old.")