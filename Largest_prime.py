def largest_prime_factor(n):
    largest_factor = 1
    
    while n % 2 == 0:
        largest_factor = 2
        n //= 2
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            largest_factor = i
            n //= i
        else:
            i += 2
            
    if n > 2:
        largest_factor = n
        
    return largest_factor