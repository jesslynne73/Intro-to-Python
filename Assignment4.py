# In this project, we will create a program that allows the user to input positive test grades to determine their
# overall average. We must ensure that the values given by the user are appropriate for the task,
# in that they are non-negative.
# Author: Jessica Strait, CMPSC 131 Sec 001

# First, we will prompt the user to begin entering their scores. I will assign this phrase a variable
# to simplify future lines of code. We will also assign variables for the total numerical value of the scores given as
# well as for the number of inputs provided.

message = "Enter a test score, or enter a negative number to receive your average."
score = int(input(message))
scores_given = 0
total = 0

# Now, we will write our while loop to ensure that the user will be prompted for as many scores as they wish to enter.
# The user will be able to stop the loop by entering any value that is less than 0, as shown in the print.

while 0 <= score:
    scores_given = scores_given+1
    total = total + float(score)
    score = int(input(message))

# For our else statement, we will need to include the calculations for determining the average through the variables
# that we have created. We also must format the answer to only include one decimal place.

else:
    print("The average of your scores is", format(float(total)/float(scores_given), ".1f"))
