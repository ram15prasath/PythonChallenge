def calculate_factorial(n):
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result = result * i
        
    return result
print(f"4! = {calculate_factorial(4)}")  
print(f"5! = {calculate_factorial(5)}")   
print(f"0! = {calculate_factorial(0)}")  