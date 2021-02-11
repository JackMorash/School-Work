while True:
    try:
        party_size = input("How many people are in your dinner party? ")
        party_size = int(party_size)
        if party_size > 8:
            print("I'm sorry, you'll have to wait for a table.")
        else:
            print("Your table is ready.")
    except ValueError:
        print("That is not a number...")
        continue
    else:
        break