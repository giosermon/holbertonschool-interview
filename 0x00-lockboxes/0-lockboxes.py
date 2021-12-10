#!/usr/bin/python3
"""
method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened.
    """
    keys = [0]
    opened = [0]
    new_key = True
    while new_key:
        new_key = False
        for box in boxes:
            if boxes.index(box) in keys:
                if boxes.index(box) not in opened:
                    opened.append(boxes.index(box))
                for k in box:
                    if k not in keys:
                        keys.append(k)
                        new_key = True
    if len(opened) == len(boxes):
        return True
    else:
        return False
