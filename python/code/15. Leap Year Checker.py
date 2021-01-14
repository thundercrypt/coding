# This program checks whether a year is a leap year or not.
year = int(input("Enter the year: "))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("The year entered is a leap year.")
        else:
            print("The year entered is not a leap year.")
    else:
        print("The year entered is a leap year.")
else:
    print("The year entered is not a leap year.")
