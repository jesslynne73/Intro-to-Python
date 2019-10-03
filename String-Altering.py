# Author: Jessica Strait
# This project utilizes string indexing rules to change a character at a set position in a string.

def mutate_string(string, position, character):
    # First, always check for type errors.
    if type(string) != str:
        return 'TypeError'
    if type(character) != str:
        return 'TypeError'
    if type(position) != int:
        return 'TypeError'
    # In string indexing, the range of a string is inclusive at the beginning and exclusive at the end. Accommodate these rules.
    first_half = string[:position]
    second_half = string[position+1:]
    # Concatenate your strings with the new character in the set position.
    new_string = first_half+character+second_half
    return new_string
