# Let's ask for the number from the user first.
num = int(input("Please enter an integer number: "))

# First let's check if it's positive.
if(num > 0):
    if(num % 2 == 0):
        print("The number is positive and divisible by 2 (even).")
    else:
        print("The number is positive and not divisble by 2 (odd).")
else:
    print("The number is not positive.")
