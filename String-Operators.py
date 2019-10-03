# Author: Jessica Strait
# This function takes in a string and evaluates what types of characters are in the string.
# It checks for alphanumeric characters, letters, digits, and identifies upper/lowercase letters.

def identify(s):
    # TypeError check
    if type(s) != str:
        return 'TypeError'
    # Establish variables
    alnum = False
    alpha = False
    digits = False
    lower = False
    upper = False
    for character in s:
        # A character cannot be a letter of number unless it is also alphanumeric.
        if character.isalnum():
            alnum = True
            if character.isalpha():
                alpha = True
                if character.isupper():
                    upper = True
                elif character.islower():
                    lower = True
            if character.isdigit():
                digits = True
        else:
            pass
    return alnum, alpha, digits, lower, upper

identify(s)
    
