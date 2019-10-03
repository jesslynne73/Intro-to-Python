# Author: Jessica Strait
# This project prints random numbers to a text file.

import random

# Next, we will ask the user how many random numbers they would like to print. We will name this variable, and we also
# name a secondary variable for our later "for" loop.

quantity = int(input("How many random numbers would you like the program to print on a random text file?"))
quantity2 = quantity

# Now, we will create our random numbers file and prepare to write in it.

text = open("random.txt", "w")

# We will create a for loop that uses the randint function from our imported random, setting the parameters between 1 
# and 500. Our for loop will also use our primary and secondary quantity variables to ensure the loop is repeated the
# necessary amount of times. Finally, we will write to our text file using the number variable that incorporates our 
# randint function.

for quantity2 in range(1, quantity+1):
    quantity2 = quantity2-1
    number = random.randint(1, 500)
    text.write(str(number)+" ")

# Once the loop has been repeated until the quantity number has been met, we will close our text file.

text.close()

# Finally, we will tell our user that the requested quantity of numbers was printed to our text file.

print(quantity, "numbers were printed to the file random.txt")
