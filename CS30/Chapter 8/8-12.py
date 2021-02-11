def make_sandwich(*items):
    """Make a sandwich with the given items."""
    print("\nLet's make a sandwich")
    for item in items:
        print(f"  ...adding {item} to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('roast beef', 'chicken', 'lettuce', 'tomato')
make_sandwich('turkey', 'cheddar cheese', 'honey mustard')
make_sandwich('strawberry jam', 'peanut butter')