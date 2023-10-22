"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        if item in frequencies:
            frequencies[item] = frequencies[item] + 1
        else:
            frequencies.update({item:1})
print(frequencies)
print("do")

    # Your code goes here
frequencies([1,1,1,1])

