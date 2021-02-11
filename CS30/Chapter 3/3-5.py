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