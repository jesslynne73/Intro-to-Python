# Author: Jessica Strait
# This project computes an average from given test scores.

# First, we will prompt the user to begin entering their scores.

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
