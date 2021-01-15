# This program calculates the table of a number up until the tenth table, using the 'for' loop.
num = int(input("Please enter a number to print its table: "))
for x in range(1,11):
    print(num,"*",x,"=",num*x)
