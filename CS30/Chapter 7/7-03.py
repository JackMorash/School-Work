while True:
    try:
        number = input("Please enter a number: ")
        number = int(number)
        if number % 10 == 0:
            print(f"{number} is a multiple of 10.")
        else:
            print(f"{number} is not a multiple of 10.")
    except ValueError:
        print("That is not a number...")
        continue
    else:
        break