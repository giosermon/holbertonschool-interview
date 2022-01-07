#!/usr/bin/python3
"""
0-minoperations.py module.
"""

def minOperations(n):
    """
    Calculates the minimum number of operations to reply n
    """

    if (n <= 0):
        return 0

    num_factor = []
    while n % 2 == 0:
        num_factor.append(2)
        n = n / 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            num_factor.append(i)
            n = n / i
    if n > 2:
        num_factor.append(n)
    return int(sum(num_factor))
