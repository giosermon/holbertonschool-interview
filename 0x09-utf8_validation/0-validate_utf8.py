#!/usr/bin/python3
"""determines if a given data set represents a valid UTF-8 encoding."""


def validUTF8(data):
    """
    args:
        @data: Integer list with the information about the character
    Return: True if the integers are UTF 8 encodable False otherwise
    """
    num = 0
    for x in data:
        mask = 0b10000000
        if not num:
            while (mask & x):
                num += 1
                mask >>= 1
            if num > 4:
                return False
            if num:
                num -= 1
                if num == 0:
                    return False
        elif num > 0:
            if x >> 6 != 2:
                return False
            num -= 1
    return not num
