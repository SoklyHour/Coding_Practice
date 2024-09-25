def memoize(func):
    """A decorator for memoizing function results."""
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]  # Return cached result if exists
        result = func(*args)  # Compute the result
        cache[args] = result   # Cache the result
        return result

    return wrapper
@memoize
def fibonacci(n):
    """Calculates the nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
print(f"Fibonacci of 10: {fibonacci(10)}")  # Output: 55
print(f"Fibonacci of 20: {fibonacci(20)}")  # Output: 6765
