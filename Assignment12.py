# In this project, we will be rewriting Assignment 9 to include popular name functions. Now that we have learned about functions in lecture, we know that this can help simplify our code.
# Author: Jessica Strait, CMPSC 131

# Let's begin by assigning some variables to the two name files we will be using, just to make our work a little bit easier.

girls = r'C:\users\jessl\Desktop\GirlNames.txt'
boys = r'C:\users\jessl\Desktop\BoyNames.txt'

# Now, let's define our getNamesList function. The function will take in either file and create a list from the information within that file.
# Don't forget to use rstrip to ignore the spaces, and to return the function as the given list. We will use this list as a parameter in our next function.


def getNamesList(filename):
    nameFile = open(filename, 'r')
    names = nameFile.readline()
    nameList = []
    while names != "":
        names = names.rstrip('\n')
        nameList.append(names)
        names = nameFile.readline()
    nameFile.close()
    return nameList


# Our second function will be the checkName function, which will determine if the name given as user input is on a list. The function will return the rank of the name, if applicable.

def checkName(name, nameList):
    if name in nameList:
        index = int((nameList.index(name) + 1))
        return index


# We will specify the name as the user's input, and create a loop that will run our two functions- note that we can use our getNamesList function as a parameter of the checkName functions.
# Now, we can use whether or not the index variable exists as a very simple "if" statement.

name = input("Enter a name to see its popularity, or enter stop to end the program.")
while name != "stop":
    if checkName(name, getNamesList(girls)):
        print(name, "is a popular girls' name and it is ranked:", checkName(name, getNamesList(girls)))
    else:
        print(name, "is not a popular girls' name.")
    if checkName(name, getNamesList(boys)):
        print(name, "is a popular boys' name and it is ranked:", checkName(name, getNamesList(boys)))
    else:
        print(name, "is not a popular boys' name.")
    name = input("Enter a name to see its popularity, or enter stop to end the program.")
