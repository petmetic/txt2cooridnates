"""
Filtering coordinates to make them easier to import into ArchiCAD for use with terrain mesh tool.
Elevation level is at least 100m above sea level, so "z" coordinates cannot be 0.00 m.
"""


f = open("input.csv", "r")
lines = f.readlines()
f.close()

# print(lines)
f = open("output.txt", "w")

for line in lines[1:]:
    coordinates = line.strip().split(",")
    # print(coordinates)
    x = coordinates[1]
    y = coordinates[2]
    z = coordinates[3]
    z1 = coordinates[4]

    if z and float(z):  # boolean operations (if True and True)
        e = z
    elif z1 and float(z1):
        e = z1
    else:
        e = None

    if e:
        print(f"{x},{y},{e}", file=f)
        #f.write(f"{x},{y},{e}\n")  # to cut into separate lines, add new line character, line separator

f.close()

"""
TRYING TO MAKE IT WORK. BOOLEANS ARE MORE ELEGANT AND EASIER... LOL!
# print(f"{x},{y},{z},{z1}")
# if float(z) != 0.000:
#   print(f"{x},{y},{z}")
# elif float(z) == 0.000:
#   print(f"{x},{y},{z1}")
# elif z1 != "":
#   print(f"{x},{y},{z},{z1}")
Didn't get to the end with this one. Missed the function which would eliminate the empty "z" coordinate.
"""
