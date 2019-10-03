# Author: Jessica Strait
# This project computes an overall average from test scores.

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

# Once a negative number is the input, we can compute the average. We also must format the answer to only include one decimal place.

print("The average of your scores is", format(float(total)/float(scores_given), ".1f"))
