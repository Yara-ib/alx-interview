#!/usr/bin/python3
""" Minimum Operations Module """


def minOperations(n: int) -> int:
    """
    Function that calculates the fewest number of operations
    needed to result in exactly n * H characters in the file

    Args:
        n (int): count needed to get as copies from the letter (H)

    Returns:
        int: number of minimum copy & paste
            operations needed to get the output = n
    """
    # In case number provided is negative=invalid
    # Or Equals 1; Then no operations needed at all
    if n <= 1:
        return 0

    count_operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            count_operations += factor
            n //= factor
        factor += 1

    return count_operations
