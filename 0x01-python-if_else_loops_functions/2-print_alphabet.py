#!/usr/bin/python3
"""Print the alphabet, not followed by a new line"""

for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
