#!/usr/bin/python3
""" Prime Game """


def set_primes(n):
    """ set_primes method set false if the number is not prime
    for each number from 0 to n
    args: 
    n: (int) the number of the elements in the list
    return: list of booleans
    """

    prime = [True for _ in range(n + 1)]
    p = 2

    while (p * p <= n):
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    return prime


def count_primes(nums):
    """ count_primes method count the number of primes in the giving list
    args:
    nums: (list) list of booleans
    return: (int) the number of primes
    """
    counter = 0
    for n in nums:
        if n:
            counter += 1

    return counter - 2


def isWinner(x, nums):
    """ isWinner method determine the winner of the game
    args:
    x: (int) the number of rounds
    nums: (list) list of integers
    return: (str) the name of the winner
    """
    if len(nums) < x or x > 10000:
        return None

    for n in nums:
        if n > 10000:
            return None

    [maria_score, ben_score] = [0, 0]

    for i in range(x):
        prime = set_primes(nums[i])
        primes_count = count_primes(prime)
        if primes_count == 0 or primes_count % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    else:
        return None
