# Write a Python program to check if a number is prime.

# prime is a number that divide by 1 and itself
def is_prime(number):
    # Numbers less than or equal to 1 are not prime
    if number <= 1:
        return False

    # Check divisibility from 2 to number - 1
    for i in range(2, number):
        if number % i == 0:
            return False

    return True

# Example usage
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

    