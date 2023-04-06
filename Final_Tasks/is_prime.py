# Write a program that generates a list of prime numbers up to a specified number.
def generate_primes(n):
    primes = []
    for number in range(2, n+1):
        is_prime = True
        for factor in range(2, int(number ** 0.5) + 1):
            if number % factor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return primes
