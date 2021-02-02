# This program calculates areas of either squares or rectangles using functions.

# Let's define our functions first.

def area_rect(length, width):
    area_rect = length * width
    print("The area of the rectangle is",area_rect,"units squared.")

def area_sq(side):
    area_sq = side**2
    print("The area of the square is",area_sq,"units squared.")

# Now let's print the program description and some instructions.

print("This program calculates the area of either a square or rectangle, depending on your choice and the dimensions of the figure so entered.")
print("Enter '1' to calculate the area of a square.")
print("Enter '2' to calculate the area of a rectangle.")

# Now let's check define the userChoice variable which will hold the choice of the user.

userChoice = int(input("Please enter your choice, as stated above: "))

# Now let's add some if, elif, and else functions.

if(userChoice == 1):
    side_sq = int(input("Enter the side of the square: "))
    area_sq(side_sq)

elif(userChoice == 2):
    length_rect = int(input("Enter the length of the rectangle: "))
    width_rect = int(input("Enter the width of the rectangle: "))
    area_rect(length_rect, width_rect)

else:
    print("Please enter a valid option after restarting the program.")
