# Course: CS 30
# Period: 1
# Date Created: 21/01/29
# Date last Modified: 21/01/29
# Name: Jack Morash
# Description: Creates a simple multiple choice menu for direction and actions

# Defines a formatted menu for directions


def print_directions():
    print(30 * "-", "DIRECTIONS", 30 * "-")
    print("1. North\n2. South\n3. East\n4. West")
    print(72 * "-")

# Defines a formatted menu for actions


def print_actions():
    print(33 * "-", "ACTIONS", 30 * "-")
    print("1. Explore\n2. Defend\n3. Attack\n4. Heal")
    print(72 * "-")

# Interprets direction inputs and invalid entries
while True:
    print_directions()
    direction = input("Please choose a direction: ").lower()
    if direction == "north":
        print("\nYou begin to head north\n")
        break
    elif direction == "south":
        print("\nYou begin to head south\n")
        break
    elif direction == "east":
        print("\nYou begin to head east\n")
        break
    elif direction == "west":
        print("\nYou begin to head west\n")
        break
    else:
        print("\nInvalid direction...\n")
        continue
# Interprets action inputs and invalid entries
while True:
    print_actions()
    direction = input("Please choose an action: ").lower()
    if direction == "explore":
        print("\nYou decide to explore\n")
        break
    elif direction == "defend":
        print("\nYou decide to defend\n")
        break
    elif direction == "attack":
        print("\nYou decide to attack\n")
        break
    elif direction == "heal":
        print("\nYou decide to heal\n")
        break
    else:
        print("\nInvalid action...\n")
        continue