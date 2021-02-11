favorite_pizzas = ['pepperoni', 'sausage', 'deep dish']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("new_pizza")
friend_pizzas.append('hawaiian')

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print(f"- {pizza}")