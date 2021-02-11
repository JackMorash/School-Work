def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_car = make_car('chevorlet', 'cavalier', color='blue', tow_package=False)
print(my_car)

my_dream_car = make_car('corvette', 'stingray', year=1963, color='gray',
                        window='split')
print(my_dream_car)
