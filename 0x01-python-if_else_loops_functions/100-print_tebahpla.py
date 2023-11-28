#!/usr/bin/python3
z = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - z)), end="")
    z = 32 if z == 0 else 0
