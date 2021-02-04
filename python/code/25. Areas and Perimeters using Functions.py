# A lot of this code has been reviewed and edited by my father, with additions from my side as well.

# Let's define the functions for executing area and perimeter.

def calculations_area(length, width, quadType):
    # Define the area variable.
    area = (length * width)
    # Print the result.
    print("The area of the", quadType, "is", area, "units squared.")

def calculations_perimeter(length, width, quadType):
    # Define the perimeter variable.
    perimeter = 2*(length + width)
    # Print the result.
    print("The perimeter of the", quadType, "is", perimeter, "units.")

# Define the inputs function, which contains almost the whole program which will run when it is called.
def inputs():
    # Print the program description and a few instructions.
    print("This program calculates the perimeter or area of either a square or rectangle, depending on your choice and the dimensions of the figure so entered.")
    print("Enter '1' to calculate the perimeter (figure will be asked later).")
    print("Enter '2' to calculate the area (figure will be asked later).")

    # Define the calcType variable to hold the variable or area choice.
    calcType = input("Please enter your choice, as stated above: ")

    # If calcType is 1, calculate the perimeter (of a given figure).
    if(calcType == "1"):

        print("Enter '1' to calculate the perimeter of a square.")
        print("Enter '2' to calculate the perimeter of a rectangle.")
        userChoice = input("Please enter your choice, as stated above: ")

        # If userChoice is 1, caclulate perimeter of square. If it is 2, calculate perimeter of a rectangle. Else, the program will restart from the inputs function.
        if(userChoice == "1"):
            length = float(input("Enter the side of the square: "))
            width = length
            calculations_perimeter(length, width, "square")

        elif(userChoice == "2"):
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            calculations_perimeter(length, width, "rectangle")

        else:
            print("                             ")
            print("This program is now restarting. Please enter a valid option.")
            print("                             ")
            inputs()
    
    # If calcType is 1, calculate the area (of a given figure).
    elif(calcType == "2"):
        print("Enter '1' to calculate the area of a square.")
        print("Enter '2' to calculate the area of a rectangle.")
        userChoice = input("Please enter your choice, as stated above: ")

        # If userChoice is 1, caclulate area of square. If it is 2, calculate area of a rectangle. Else, the program will restart from the inputs function.
        if(userChoice == "1"):
            length = float(input("Enter the side of the square: "))
            width = length
            calculations_area(length, width, "square")

        elif(userChoice == "2"):
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            calculations_area(length, width, "rectangle")

        else:
            print("                             ")
            print("This program is now restarting. Please enter a valid option.")
            print("                             ")
            inputs()
    # If the user enters anything other than 1 or 2, restart the program from the inputs function.
    else:
        print("                             ")
        print("This program is now restarting.Please enter a valid option.")
        print("                             ")
        inputs()

# Now call the function 'inputs'.
inputs()
