# Author: Jessica Strait
# This project provides customers with the price of a software purchase while accounting for a volume discount.

# First, the program will ask the user the number of software packages that they have purchased.

value = int(input("Enter the number of packages ordered."))

# Now, we will assign the original cost of any purchase before a volume discount. We know that this will be $100 times
# however many packages were purchased, which is the variable "value."

initial = value*100

# Next, we will tell the program what discounts to apply to the total cost based on the quantity input provided.
# We will use elif statements to account for each range of discounts. Then, the program will print both the total cost
# of the purchase including the discount, as well as how much the discount was for.

if value <=9 :
    discount = 0
    print("The cost of your purchase was $"+format(value*100, ".2f"), "with a discount of $"+format(discount, ".2f"))
elif 10 <= value <= 19:
    discount = initial*0.1
    total = initial - discount
    print("The cost of your purchase was $"+format(total, ".2f"), "with a discount of $"+format(discount, ".2f"))
elif 20 <= value <= 49:
    discount = initial*0.2
    total = initial - discount
    print("The cost of your purchase was $"+format(total, ".2f"), "with a discount of $"+format(discount, ".2f"))
elif 50 <= value <= 99:
    discount = initial*0.3
    total = initial - discount
    print("The cost of your purchase was $"+format(total, ".2f"), "with a discount of $"+format(discount, ".2f"))
elif value >= 100:
    discount = initial*0.4
    total = initial - discount
    print("The cost of your purchase was $"+format(total, ".2f"), "with a discount of $"+format(discount, ".2f"))
