def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_list = [0, 1]

    for i in range(2, n):
        next_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(next_fib)      
    return fib_list

print(f"n=0: {generate_fibonacci(0)}") 
print(f"n=1: {generate_fibonacci(1)}")  
print(f"n=5: {generate_fibonacci(5)}")  
print(f"n=8: {generate_fibonacci(8)}")  