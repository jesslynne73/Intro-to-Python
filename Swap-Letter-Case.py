# Author: Jessica Strait
# This function takes a string as input. It makes all uppercase letters lowercase and all lowercase letters uppercase.

def swap_case(s):
    # Always do a type error check.
    if type(s) != str:
      return 'TypeError'
    # Initialize an empty string.
    answer = ''
    # Use string operations to check all elements of the string to determine case, if applicable.
    for index in range(len(s)):
        character = s[index]
        if character.isupper():
            # Append altered characters to the empty answer string.
            answer += character.lower()
        elif character.islower():
            answer += character.upper()
        elif character.isalpha() is False:
            answer += character
    return answer

s = input()
result = swap_case(s)
print(result)
