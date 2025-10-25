def even_numbers():
    """
    An infinite generator that yields non-negative even integers starting from 0.
    """
    n = 0
    while True:
        yield n
        n += 2

# --- Example Usage (To test the infinite generator) ---

# 1. Create the generator object
even_gen = even_numbers()

# 2. Use the next() function to get values one by one
print(f"First: {next(even_gen)}")  # Output: 0
print(f"Second: {next(even_gen)}") # Output: 2

# 3. Use a for loop to get the next few values (must limit the loop!)
print("Next 5 values:")
for _ in range(5):
    print(next(even_gen))