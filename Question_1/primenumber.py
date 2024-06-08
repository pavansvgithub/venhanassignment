def is_prime(n):
    factors = 0 
    for i in range(2,n):
        if n % i == 0:
            factors += 1 
    if factors == 0:
        return "Prime Number"
    else:
        return "Not a prime Number"

number = int(input())
result = is_prime(number)
print(result)