
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

#TODO seive of eratosthenis

if __name__ == "__main__":
    print(generate_primes(0, 15))