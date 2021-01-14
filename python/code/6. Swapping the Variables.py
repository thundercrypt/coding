# Let's define two variables.
intOne = 5
intTwo = 8

print("The value of the first variable is ",intOne,", and the value of the second variable is ",intTwo,".")

# We have to swap the values of the two variables.
# To do so, let's introduce a third variable and define its value as 0.
intThree = 0

# Now, let's swap.

intThree = intOne
# Now the value of intThree is 5.

intOne = intTwo
# And now the value of intOne is 8.

intTwo = intThree
# And now the value of intTwo is 5.

print("The value of the first variable after swapping is ",intOne,", and the value of the second variable after swapping is ",intTwo,".")
