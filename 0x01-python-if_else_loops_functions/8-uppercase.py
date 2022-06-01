#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i >= "a" or i <= "z":
            print("{}".format(chr(ord(i) - 32)), end="")
    print()
