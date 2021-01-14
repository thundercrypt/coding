# This program calculates the grade of the user as per hs marks entered.
userMarks = float(input("Please enter your marks: "))

# Let's use shorthand.
if(userMarks<=100.0 and userMarks>=80.0): print("Grade A.")
elif(userMarks<80.0 and userMarks>=60.0): print("Grade B.")
elif(userMarks<60.0 and userMarks>=40.0): print("Grade C.")
elif(userMarks<40.0 and userMarks>=00.0): print("Grade D.")
else: print("Please enter valid marks, between 100 and 0 (can be decimals).")
