# This program displays the natural predecessors of a number entered using the while loop.
userInput = int(input("Please enter a number to print its natural predecessors: "))

sum = 0
predecessor = 1

while(predecessor <= userInput):
    sum = sum + predecessor
    i = i + 1                           # Update the counter

print("The sum is",sum)
