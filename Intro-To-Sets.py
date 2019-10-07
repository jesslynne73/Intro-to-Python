# Author: Jessica Strait
# This is an exercise in the set data type: an unordered group of elements in which no element repeats.
# This program will take a list of integers, create a set of the distinct values, and average all distinct elements.

def average(array):
    # Instantiate an empty set and the Boolean variable we will use.
    set = []
    equivalence = False
    # Traverse the list and append all unique values to the empty set.
    for number in array:
        for value in set:
            if number != value:
                equivalence = False
            else:
                equivalence = True
                break
        if equivalence is True:
            pass
        else:
            set.append(number)
    # Create variables for the sum of the numbers and the number of elements.
    sum = 0
    length = len(set)
    for number in set:
        sum += number
    final_solution = sum/length
    return final_solution


n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)
