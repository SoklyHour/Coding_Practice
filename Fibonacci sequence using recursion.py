# How do you print a Fibonacci sequence using recursion?
# The Fibonacci sequence is a series of numbers where each number 
# is the sum of the two preceding ones. You can print it using recursion

def print_fibonacci(n, a=0, b=1):
    if n == 0:
        return  # Base case: If n is 0, stop the recursion
    print(a)  # Print the current Fibonacci number
    print_fibonacci(n-1, b, a + b)  # Recursively call with next Fibonacci numbers
    
print(print_fibonacci(10))