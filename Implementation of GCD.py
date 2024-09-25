# The Greatest Common Divisor (GCD) of two numbers is the largest number that divides both of them without leaving a remainder.
def gcd(a, b):
    """Calculate the GCD of two numbers using the Euclidean algorithm."""
    while b != 0:
        a, b = b, a % b  # Update a to b, and b to the remainder of a divided by b
    return a

# Example usage
num1 = 48
num2 = 18
result = gcd(num1, num2)

print(f"The GCD of {num1} and {num2} is: {result}")
