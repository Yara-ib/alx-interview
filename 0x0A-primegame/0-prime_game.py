#!/usr/bin/python3
""" Prime Game Module """


def is_Prime(n):
    """
    Using Sieve of Eratosthenes method to get prime numbers

    Args:
        n (int): last number in the last to check

    Returns:
        list[int]: list of prime numbers
    """
    # Assuming all true at first, then change it later
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    # Starting from 2; 1st prime number
    # int(n**0.5); because the square root of the last number if checked,
    # i won't have to check all the other multipliers
    for i in range(2, int(n**0.5) + 1):
        # To skip the already checked as false
        if primes[i]:
            # To check the multiples of each number too
            for multiples in range(i**2, n + 1, i):
                primes[multiples] = False

    return primes


def isWinner(x, nums):
    """
    Checks who's the winner in the Prime Game

    Args:
        x (int): number of rounds
        nums (list[int]): array of no. of set of consecutive integers
                            from 1 up to & including n

    Returns:
        str: name of the player that won the most rounds
    """
    if not nums or x <= 0:
        return None

    primes = is_Prime(max(nums))
    maria_score = ben_score = 0

    for num in nums:
        not_removed_yet = [True] * (num + 1)
        maria_picks_num = True

        while True:
            got_prime_in_list = False

            for i in range(2, num + 1):
                if primes[i] and not_removed_yet[i]:
                    got_prime_in_list = True
                    for multiples in range(i, num + 1, i):
                        not_removed_yet[multiples] = False
                    break

            if not got_prime_in_list:
                if maria_picks_num:
                    ben_score += 1
                else:
                    maria_score += 1
                break

            # Switching between who picks the number
            maria_picks_num = not maria_picks_num

    if maria_score > ben_score:
        return "Maria"
    elif maria_score < ben_score:
        return "Ben"
    else:
        return None
