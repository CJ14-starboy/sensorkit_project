"""
Module: sensorkit/stats.py
Contributor: Kofi Nyamekye Owusu-Mensah
Student ID: 64712029
Date: Wednesday 5th August 2026
Role: Simple summary statistics for a list of numeric readings.

Complete the TODOs below.
"""


def mean(values):
    if len(values)<= 0:
        raise ValueError("mean() needs values")
    else:
        Total= sum(values)
        num= len(values)
        Average= Total/num
        return Average


def minimum(values):
    least_val= min(values)
    return least_val


def maximum(values):
    high_val= max(values)
    return high_val


def spread(values):
    Spread= maximum(values) - minimum(values)
    return Spread

list1 = [2, 4, 6, 8]
print(spread(list1))
