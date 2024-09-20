#!/usr/bin/python3
""" Change comes from within Module """


def makeChange(coins, total):
    """
    Get the fewest number of coins needed to meet a given amount total

    Args:
        coins (list[int]): List of the values of the coins in your possession
        total (int): Given amount

    Returns:
        int: fewest number of coins needed to meet total
    """

    if total <= 0:
        return 0

    countNeeded = 0
    trackCoinsCount = 0
    # To check the largest value coin getting the least coins needed
    coins.sort(reverse=True)

    for coin in coins:
        trackCoinsCount = total // coin
        countNeeded += trackCoinsCount
        total -= trackCoinsCount * coin

        if total == 0:
            return countNeeded

    if total > 0:
        return -1
