
def generate_primes(start, end):
    """Generates prime numbers between start and end values."""

    primes = []

    for i in range(start, end):
        isPrime = True
        if i < 2:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    isPrime = False
                    break
            if isPrime:
                primes.append(i)

    
    return primes


def sieve_of_erato(num):
    
    primes = [True for _ in range(num + 1)]

    toRet = []

    p = 2

    while p * p <= num:

        if primes[p] is True:

            for i in range(p*p, num+1, p):

                primes[i] = False

        p+=1
    
    for i in range(1, num+1):
        if primes[i] is True:
            toRet.append(i)

    return toRet




if __name__ == "__main__":
    print(generate_primes(0, 15))
    print(sieve_of_erato(15))