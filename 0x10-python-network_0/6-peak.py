#!/usr/bin/python3
"""Finds a peak in an unsorted list of integers."""


def find_peak(list_of_integers):
    """
    Finds a peak in an unsorted list of integers.
    Args:
        list_of_integers (list[int]): The input list of integers.
    Returns:
        int: The peak element found in the list.
    Complexity:
        The algorithm has O(log(n)) complexity.
    """
    if not list_of_integres:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = left + (right - left) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
