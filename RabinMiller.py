# Implements the RabinMiller primality test with the first seven primes. Provably correct for inputs < 3.4 * 10^14.

# Imports
import math

# CONSTANTS
PRIME_SET = {2,3,5,7,11,13,17}

# Counts the factors of two dividing the passed in input
def countFactorsOfTwo(x):
    result = 0
    while math.fmod(x,2) == 0:
        x /= 2.0
        result += 1
    return(result)

# Checks to see if the input is prime.
def testInput(x):
    if x == 2 or x == 3:
        return(True)
    if x % 2 == 0 or x % 3 == 0:
        return(False)
    evenPower = int(countFactorsOfTwo(x - 1))
    oddFactor = int((x - 1) / 2**evenPower)
    for p in [prime for prime in PRIME_SET if prime < x]:
        if pow(p,oddFactor,x) == 1:
            return(True)
        for j in range(0,evenPower):
            if pow(p,(2**j)*oddFactor,x) == x-1:
                return(True)
    return(False)