import math

# Get user input
N = int(input("Enter an integer: "))

# Handle edge cases
if N <= 1:
    is_prime = False
else:
    is_prime = True
    for i in range(2, int(math.isqrt(N)) + 1):
        if N % i == 0:
            is_prime = False
            break

# Display result
if is_prime:
    print(N, "is a prime number.")
else:
    print(N, "is not a prime number.")