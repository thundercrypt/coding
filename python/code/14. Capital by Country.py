# This program gives the capital of the country entered by the user.
userCountry = input("Please enter a Country Name: ")

if("India" in userCountry): print("The capital of",userCountry,"is New Delhi.")
elif("Australia" in userCountry): print("The capital of",userCountry,"is Canberra.")
elif("France" in userCountry): print("The capital of",userCountry,"is Paris.")
elif("Japan" in userCountry): print("The capital of",userCountry,"is Tokyo.")
else: print("Please enter a country included in the database.")
