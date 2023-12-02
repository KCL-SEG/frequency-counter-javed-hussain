"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    result_dict = {}

    for item in items:
        # Convert non-string items to string for dictionary key
        key = str(item) if not isinstance(item, str) else item

        # Update the dictionary with the key and count its occurrences
        result_dict[key] = result_dict.get(key, 0) + 1

    return result_dict

    # Your code goes here


