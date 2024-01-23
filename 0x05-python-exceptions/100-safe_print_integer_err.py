#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    res = True
    try:
        print("{:d}".formatv(value))
    except Exception as ex:
        print("Exception:", ex, file=sys.stderr)
        res = False
    return res
