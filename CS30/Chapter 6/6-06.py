favorite_languages = {
    'jack': 'python',
    'arden': 'javascript',
    'arsal': 'PHP',
    'ali': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")

coders = ['jack', 'arden', 'arsal', 'ali', 'ahmed', 'james', 'jacqeus']
for coder in coders:
    if coder in favorite_languages.keys():
        print(f"Thank you for taking the poll, {coder.title()}!")
    else:
        print(f"{coder.title()}, what's your favorite programming language?")