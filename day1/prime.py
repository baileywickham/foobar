def isPrime(n) :
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True

    if (n % 2 == 0 or n % 3 == 0) :
        return False

    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6

    return True

def solution(i):
    primestr = ''
    # Generate first 10k primes
    for p in range(1047300):
        if isPrime(p):
            primestr += str(p)
            if len(primestr) >= i + 5:
                break

    return primestr[i:i+5]




