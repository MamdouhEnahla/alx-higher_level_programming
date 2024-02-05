#!/usr/bin/python3
""" inherits the list class """


class MyList(list):
    """prints the list sorted (ascending sort)"""

    def print_sorted(self):
        '''prints sorted list'''
        print(sorted(self))
