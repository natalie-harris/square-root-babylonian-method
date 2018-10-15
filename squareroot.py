#calculates square root of any real positive integer using the 'babylonian square root method'
print("")
print("This program calculates the square root of any real positive integer using the 'babylonian square root method'")

#imports necessary modules
import math

#sets up variables
isPosInt = False

#while loop to ask for a positive integer to find the square root
while isPosInt == False:
	base = int(raw_input("What is the base number you want to find the square root of? "))
	if str.isdigit(str(base)) == True:
		isPosInt = True
	else:
		isPosInt = False
		print("The base number must be a positive integer")
		print("")
	if base == 0 or base == 1:
		isPosInt = False
		print("The square root of " + str(base) + " is " + str(base))
		print("")

#find the guess of whatever the number is
if base < 10:
	guess = base
	guess = float(str(guess) + (".000"))
elif base < 100:
	guess = int(math.ceil(base / 2))
	guess = float(str(guess) + (".000"))
elif base < 1000:
	guess = int(math.ceil(base / 4))
	guess = float(str(guess) + (".000"))
elif base < 10000:
	guess = int(math.ceil(base / 8))
	guess = float(str(guess) + (".000"))
elif base < 100000:
        guess = int(math.ceil(base / 16))
        guess = float(str(guess) + (".000"))
elif base < 1000000:
        guess = int(math.ceil(base / 32))
        guess = float(str(guess) + (".000"))
elif base < 10000000:
        guess = int(math.ceil(base / 64))
        guess = float(str(guess) + (".000"))
elif base < 100000000:
        guess = int(math.ceil(base / 128))
        guess = float(str(guess) + (".000"))

#finds the square root of the base
while guess != ((guess + (base / guess)) / 2):
	guess = ((guess + (base / guess)) / 2)

#prints the square root
print("")
print("The square root of " + str(base) + " is " + str(guess))
