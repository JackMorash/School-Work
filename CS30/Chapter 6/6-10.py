favorite_numbers = {
    'jack': [42, 17],
    'arden': [69, 3549, 34],
    'ali': [7, 122],
    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f"  {number}")