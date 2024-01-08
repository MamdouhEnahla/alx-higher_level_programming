#!/usr/bin/python3
def islower(c):
    return (ord(c) >= ord('a') and ord(c) <= ord('z'))


def uppercase(str):
    for c in str:
        print("{:c}"
              .format(ord(c) if not islower(c) else ord(c) - 32),
              end="")
    print("")
