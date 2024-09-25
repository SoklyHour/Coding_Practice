# How do you check if an integer is even or odd?
# You can check if an integer is even by dividing it by 2 and checking the remainder.
def is_even(number):
    return number % 2 == 0
    

print(is_even(4))   # Output: True
print(is_even(7))   # Output: False
print(is_even(0))   # Output: True
print(is_even(-2))  # Output: True
print(is_even(-3))  # Output: False

