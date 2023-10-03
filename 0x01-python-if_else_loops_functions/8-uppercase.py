#!/usr/bin/python3
def uppercase(str):
    for upper in str:
        if ord(upper) <= ord('z') and ord(upper) >= ord('a'):
            ch = chr(ord(upper) - 32)
        else:
            ch = upper
        print("{:s}".format(ch), end="")
    print('')
