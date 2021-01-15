# This program takes a few values from the user and then cacluates the areas of squares and rectangles from the dimensions given.
sidesq = float(input("Enter the side of the square in meters: "))
lengthrect = float(input("Enter the length of the rectangle here in meters: "))
widthrect = float(input("Enter the width of the rectangle here in meters: "))
arsq = sidesq*sidesq                                # We can also use 'sidesq**2'
arrect = lengthrect*widthrect
# Processes values
print("Processing...")
# Prints values
print("The area of the square is:",arsq,"meters squared.")
print("The area of the rectangle is:",arrect,"meters squared.")
