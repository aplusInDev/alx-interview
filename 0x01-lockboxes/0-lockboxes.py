#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists. Each index contains a list of integers.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not isinstance(boxes, list):
        return False

    if len(boxes) == 0:
        return False

    if len(boxes) == 1:
        return True

    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)

    if len(keys) == len(boxes):
        return True
    else:
        return False
