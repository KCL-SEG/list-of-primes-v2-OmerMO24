"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
    else:
        return False
    
    return True

def primes(number_of_primes):
    list = []
    # add the first number_of_primes primes to the list
    if number_of_primes <= 0:
        raise ValueError("number_of_primes must be greater than 0")
    i = 2
    while len(list) < number_of_primes:
        if isPrime(i):
            list.append(i)
        i += 1
    return list
