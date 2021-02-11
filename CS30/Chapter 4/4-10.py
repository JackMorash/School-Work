cubes = []

for value in range(1, 11):
  cube = value ** 3
  cubes.append(cube)
print(cubes)

print("The first three items in the list are:")
for value in cubes[:3]:
  print(value)

print(f"\nThree items from the middle of the list are:")

for value in cubes[4:-3]:
  print(value)

print(f"\nThe last three items in the list are:")
for value in cubes[-3:]:
  print(value)