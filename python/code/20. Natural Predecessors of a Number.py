# This program displays the natural predecessors of a number entered using the while loop.
userInput = int(input("Please enter a number to print its natural predecessors: "))

predecessor = 1

while(predecessor < userInput):
    print(predecessor)
    predecessor = predecessor + 1                           # Update the counter


