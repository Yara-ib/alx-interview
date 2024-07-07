#!/usr/bin/python3
""" LockBoxes Module """
from typing import List


def canUnlockAll(boxes: List[List]) -> bool:
    """
    Method to determines if all the boxes can be opened or not

    Args:
        boxes (List[List]): List of boxes includes list of boxes
                    each needs a key to open

    Returns:
        bool: True if all boxes can be opened || False
    """

    # Assuming that all the boxes weren't checked(visited) yet
    # So giving them all value of False(not visited)
    # to initialize the process
    visited_Boxes = [False] * len(boxes)

    def depth_first_search(box: List) -> None:
        """
        Using Depth First Search Technique
        & recursion to check the visited boxes

        Args:
            box (List): A box of keys as a part of other list[boxes]

        Returns:
            bool: True || False if visited box or Not
        """

        # Assuming the first box @each round is unlocked(visited)
        visited_Boxes[box] = True
        for key in boxes[box]:
            # Side Note: key with the same number as a box opens that box
            if key < len(boxes) and not visited_Boxes[key]:
                # Recursion over all keys in each box to be checked
                depth_first_search(key)

    # Checking each box @round in the main function using the helper method
    depth_first_search(0)

    # Checking the List of the visited_Boxes
    # if all values saved were True(visited) || Not
    return all(visited_Boxes)
