#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".formatv(value))
        return True
    except Exception as ex:
        print("Exception:", ex, file=sys.stderr)
        return False
