guests = ['Bill Gates', 'Niclas Mouritzen', 'Mehdi Sadaghdar']

person = guests[0].title()
print(f"{person}, You have been invited to a dinner!.")

person = guests[1].title()
print(f"{person}, You have been invited to a dinner!.")

person = guests[2].title()
print(f"{person}, You have been invited to a dinner!.")

person = guests[1].title()
print(f"\nSorry, {person} can't make it to the dinner.")

# Niclas was unable to attend, his invitation was given to Michael

del(guests[1])
guests.insert(1, 'Michael Grzesiek')

# Re-prints invitations

person = guests[0].title()
print(f"\n{person}, You have been invited to a dinner!.")

person = guests[1].title()
print(f"{person}, You have been invited to a dinner!.")

person = guests[2].title()
print(f"{person}, You have been invited to a dinner!.")

# Word got around, turns out lots of people want to attend...

print("\nWord got around, turns out lots of people want to attend...")
guests.insert(0, 'Benjamin Rich')
guests.insert(2, 'Todd Howard')
guests.append('Queen Elizabeth II')

person = guests[0].title()
print(f"{person}, You have been invited to a dinner!.")

person = guests[1].title()
print(f"{person}, You have been invited to a dinner!.")

person = guests[2].title()
print(f"{person}, You have been invited to a dinner!.")

person = guests[3].title()
print(f"{person}, You have been invited to a dinner!.")

person = guests[4].title()
print(f"{person}, You have been invited to a dinner!.")

person = guests[5].title()
print(f"{person}, You have been invited to a dinner!.")

# Unfortunately, new Covid-19 restrictions have limited our guests

print("\nUnfortunately, only two people can come to the dinner")

person = guests.pop()
print(f"Sorry, {person.title()} there's no room at the table.")

person = guests.pop()
print(f"Sorry, {person.title()} there's no room at the table.")

person = guests.pop()
print(f"Sorry, {person.title()} there's no room at the table.")

person = guests.pop()
print(f"Sorry, {person.title()} there's no room at the table.")

# Two people remain for invitation

person = guests[0].title()
print(f"{person}, You have been invited to a dinner!.")

person = guests[1].title()
print(f"{person}, You have been invited to a dinner!.")

# Clears some members of the list

del(guests[0])
del(guests[0])

# Reprints empty list

print(guests)