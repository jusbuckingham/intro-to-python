'''
/***********************************************************************
In these exercises we will be practicing decomposition by building
multiple functions. Be sure to test each function thoroughly as you go
before moving on to the next problem. Each function will require the
previous to solve.
***********************************************************************/
'''


'''
/***********************************************************************
Write a function `is_prime(number)` that returns a boolean indicating if
`number` is prime or not. Assume `number` is a positive integer.

Examples:

print(is_prime(2)) # => True
print(is_prime(1693)) # => True
print(is_prime(15)) # => False
print(is_prime(303212)) # => False
***********************************************************************/
'''


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            return True


print(is_prime(2))  # => True
print(is_prime(1693))  # => True
print(is_prime(15))  # => False
print(is_prime(303212))  # => False


'''
/***********************************************************************
Using the `is_prime` function you made, write a function `first_n_primes(n)`
that returns an array of the first `n` prime numbers.

Examples:

print(first_n_primes(0)) # => []
print(first_n_primes(1)) # => [2]
print(first_n_primes(4)) # => [2, 3, 5, 7]
***********************************************************************/
'''


def first_n_primes(n):
    primes = []
    num = 2

    while (len(primes)) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


print(first_n_primes(0))  # => []
print(first_n_primes(1))  # => [2]
print(first_n_primes(4))  # => [2, 3, 5, 7]

'''
/***********************************************************************
 Using `first_n_primes`, write a function `sum_of_n_primes(n)` that returns
the sum of the first `n` prime numbers.

Examples:

print(sum_of_n_primes(0)) # => 0
print(sum_of_n_primes(1)) # => 2
print(sum_of_n_primes(4)) # => 17
***********************************************************************/
'''


def sum_of_n_primes(n):
    sum = 0
    primes = first_n_primes(n)
    for i in range(0, len(primes)):
        sum = sum + primes[i]
    return sum


print(sum_of_n_primes(0))  # => 0
print(sum_of_n_primes(1))  # => 2
print(sum_of_n_primes(4))  # => 17