import importTest
from importTest import my_dream_car
from importTest import my_car as m
import importTest as mdc
from importTest import *

print(m.my_car)
print(my_dream_car)
mdc
# Note that repl interprets star imports wierdly
# and underlines it despite having seemingly no issue
my_dream_car = make_car('corvette', 'stingray', year=1963, color='gray',
                        window='split')
print(my_dream_car)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)