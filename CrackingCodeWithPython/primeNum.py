#Prime Number Sieve
#www.nostarch.com/crackingcodes/

import math, random

def isPrimeTrialDiv(num):
    #return true if num is a prime num else false
    #uses the trial division algorithm for testing primality
    #numbers less than 2 are not prime
    if num < 2:
        return False
    
    #see if num is divisible by any number up to the sqr root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    
    return True

def primeSieve(sieveSize):
    #returns a list of prime numbers calculated using the sieve of eratosthenes algorithm 

    sieve = [True] * sieveSize
    #0 and 1 are not prime numbers 
    sieve[0] = False
    sieve[1] = False

    #create sieve
    for i in range(2, int(math.sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i

    #compile the list of primes
    primes = []
    for i in range(sieveSize):
        if sieve[i] == True:
            primes.append(i)

    return primes

def rabinMiller(num):
    #return true if num is a prime number
    if num % 2 == 0 or num < 2:
        return False
    if num == 3:
        return True

    s = num - 1
    t = 0
    while s % 2 == 0:
        #keep halving until num is odd, t is used to count how many times we halve s
        s = s // 2
        t += 1

    for trials in range(5): #try to falsify nums primality 5 times
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)

        if v != 1: #test doesnt apply if v is 1
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num

    return True

#most of the time you can quickly find if a number is prime by dividing by the 
#first few dozen prime numbers this is quicker than rabinMiller() but doesnt always work

LOW_PRIMES = primeSieve(100)

def isPrime(num):
    #returns true is num is prime, does a quick prime check before calling rabinMiller
    if (num < 2):
        return False #0, 1 and negative are not prime
    #see if low numbers divide
    for prime in LOW_PRIMES:
        if (num == prime):
            return True
        if (num % prime == 0):
            return False
    #if all else fails call rabinMiller() to determine if prime
    return rabinMiller(num)

def generateLargePrime(keysize=1024):
    #return a random prime number that is keysize bits in size
    while True:
        num = random.randrange(2**(keysize-1), 2**(keysize))
        if isPrime(num):
            return num

