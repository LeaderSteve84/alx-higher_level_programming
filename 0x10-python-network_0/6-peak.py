#!/usr/bin/python3
"""finds a peak"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1
    while left < right:
        mid = (left + right) // 2

        # compare mid with it neighbour to find the peak
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1
        return list_of_integers[left]
