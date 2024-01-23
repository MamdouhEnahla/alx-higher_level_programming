#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    res = None
    try:
        res = fct(args[1:])
    except Exception as ex:
        print("Exception:", ex, file=sys.stderr)
    return res
