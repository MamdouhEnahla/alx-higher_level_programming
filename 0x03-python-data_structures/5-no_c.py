#!/usr/bin/python3
def no_c(my_string):
    res = ""
    for ch in my_string:
        if ch not in "Cc":
            res += ch
    return res
