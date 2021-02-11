# Course: CS 30
# Period: 1
# Date Created: 21/01/12
# Date last Modified: 21/01/12
# Name: Jack Morash
# Description: Creates an inventory of items and organizes said list

# Creates an empty list for each item type in the inventory

food = []
weapons = []
potions = []

# Adds a potion to the inventory

potions.insert(0, 'Swiftness Potion')
print(f"\nYou have discovered a {potions[0]}!")
print(potions)

# Adds another potion to the inventory

potions.append('Healing Potion')
print(f"\nYou have discovered a {potions[1]}!")
print(potions)

# Sorts the potions alphabetically

print("You decide to sort your potions")
potions.sort()
print(potions)

# Sorts the potions in reverse alphabetical order

print("You decide to sort your potions in reverse alphabetical order")
potions.sort(reverse=True)
print(potions)

# Removes a potion after drinking it

print(f"\nYou have drank the {potions[1]}!")
potions.remove(potions[1])
print(potions)

# Adds a loaf of bread and an apple to the inventory

food.insert(0, 'Loaf of Bread')
print(f"\nYou have discovered a {food[0]}!")
print(food)

food.insert(1, 'Apple')
print(f"\nYou have discovered an {food[1]}!")
print(sorted(food))
# Checks the amount of items in the inventory

print("You decide to check how many potions you have")
print(f"\nYou have {len(potions)} potions")

# The apple is moved to your backpack

backpack_item = food.pop(1)
print(f"\nYou moved your {backpack_item} to your backpack")
print(food)

# The loaf of bread is stolen by a bird and removed from the inventory

print(f"\nA bird has stolen your {food[0]}")
del food[0]
print(food)