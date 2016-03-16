# Imports
import RabinMiller

# Constants
TEST_UP_TO = 10000000

# Accepts an integer and returns true iff it is pandigital
def isPandigital(x):
    toCheck = str(x)
    for digit in range(1,len(toCheck) + 1):
        if str(digit) not in toCheck:
            return False
    return True

# finds the largest pandigital prime
def main():
    for prime in [p for p in range(TEST_UP_TO,2,-1) if RabinMiller.testInput(p)]:
        if isPandigital(prime):
            print(prime)
            return

main()