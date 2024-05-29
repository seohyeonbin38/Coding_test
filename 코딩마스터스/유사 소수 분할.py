def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_pseudo_primes(limit):
    pseudo_primes = []
    for i in range(2, limit):
        for j in range(i + 1, limit):
            if is_prime(i) and is_prime(j):
                pseudo_prime = i * j
                if pseudo_prime < limit:
                    pseudo_primes.append(pseudo_prime)
                else:
                    break
    return list(set(pseudo_primes))

def can_be_partitioned(n, pseudo_primes):
    pseudo_primes_set = set(pseudo_primes)
    
    for i in range(1, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                l = n - i - j - k
                if l > k:
                    count = sum([num in pseudo_primes_set for num in [i, j, k, l]])
                    if count >= 3:
                        return True
    return False

def main():
    N = int(input().strip())
    
    if N < 4:
        print("impossible")
        return
    
    pseudo_primes = generate_pseudo_primes(N)
    
    if can_be_partitioned(N, pseudo_primes):
        print("possible")
    else:
        print("impossible")

if __name__ == "__main__":
    main()
