rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'America'
    }

for name, river in rivers.items():
    print(f"The {name.title()} river runs through {river.title()}.")

print()

print("Countries:")
for country in rivers.values():
    print(country.title())

print()

print("Rivers:")
for name in sorted(rivers.keys()):
    print(f"{name.title()}")