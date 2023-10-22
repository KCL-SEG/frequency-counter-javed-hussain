"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        if frequencies[item] > 0:
            frequencies.update({item:0})
        else:
            frequencies[item] = frequencies[item] + 1


    # Your code goes here
    print(frequencies)

frequencies([2,3,2])