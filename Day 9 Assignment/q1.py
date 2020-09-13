"""
The following module contains a function for checking whether a number is prime or not.
"""
N = 100
def check_prime(number):
    """
    Checks whether the given number is prime or not
    """
    if number <= 1:
        return False
    for element in range(2, number):
        if number % element == 0:
            return False
    return True
check_prime(N)
