#calculates square root of any real positive integer using the 'babylonian square root method'
print("\nThis program calculates the square root of any real positive integer using the 'babylonian square root method'")

#imports necessary modules
import math

#sets up variables
isPosInt = False

#while loop to ask for a positive integer to find the square root
while isPosInt == False:
	base = raw_input("What is the base number you want to find the square root of? ")
	if str.isdigit(str(base)) == True:
		base = int(base)
		isPosInt = True
	else:
		isPosInt = False
		print("The base number must be a positive integer\n")
	if base == 0 or base == 1:
		isPosInt = False
		print("The square root of " + str(base) + " is " + str(base) + "\n")

#find the guess of whatever the number is
length = (len(str(base)))
guess = int(math.ceil(base / (2 ** length)))
guess = float(str(guess) + (".000"))

#finds the square root of the base
while guess != ((guess + (base / guess)) / 2):
	guess = ((guess + (base / guess)) / 2)

#prints the square root
print("\nThe square root of " + str(base) + " is " + str(guess) + "\n")
