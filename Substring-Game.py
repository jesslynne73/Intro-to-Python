# Author: Jessica Strait. Prompt adapted from HackerRank 'The Minion Game.'
# Jess and Drew want to play the 'The Substring Game'.
# Both players are given the same string, and they have to make substrings using the letters of the string .
# Jess has to make substrings starting with consonants, and Drew has to make substrings starting with vowels.
# The game ends when both players have made all possible substrings.

# A player gets +1 point for each occurrence of the substring in the string .
# String  = BANANA
# Drew's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Drew will get 2 Points.

#Determine the winner of the game and their score with the string as input.

def substring_game(string):
    # Check for a type error.
    if type(string) != str:
        return 'TypeError'
    # Y will count as a consonant in the game.
    vowels = 'AEIOU'
    # Initialize player's scores to zero
    Drew_vowels = 0
    Jess_consonants = 0
    for value in range(len(string)):
        if string[value] in vowels:
            # If a letter is identified as a vowel, Drew could make substrings at each index remaining in the string.
            Drew_vowels += len(string)-value
        else:
            Jess_consonants += len(string)-value
    # Compare scores to determine the winner.
    if Drew_vowels > Jess_consonants:
        return 'Drew '+str(Drew_vowels)
    elif Jess_consonants > Drew_vowels:
        return 'Jess '+str(Jess_consonants)
    elif Drew_vowels == Jess_consonants:
        return 'Draw'

   s = input()
   print(substring_game(s))
