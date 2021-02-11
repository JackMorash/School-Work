# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'cat',
    'name': 'sparky',
    'owner': 'john',
    'weight': 41,
    'eats': 'cat food',
}
pets.append(pet)

pet = {
    'animal type': 'fish',
    'name': 'gubbles',
    'owner': 'jack',
    'weight': 1.5,
    'eats': 'fish flakes',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'max',
    'owner': 'sam',
    'weight': 37,
    'eats': 'homework',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")