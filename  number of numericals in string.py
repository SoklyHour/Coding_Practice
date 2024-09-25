# How can you compute the number of numericals in a string?

# You can inspect each character within the string by 
# utilising the isdigit() method to determine if it’s a numeral.

def count_numerical_digits(input_string):
    count = 0
    for char in input_string:
        if char.isdigit():
            count += 1
    return count

print(count_numerical_digits("Hello123"))     # Output: 3
print(count_numerical_digits("No numbers!"))   # Output: 0
print(count_numerical_digits("1234567890"))    # Output: 10
print(count_numerical_digits("Room 101"))      # Output: 3
print(count_numerical_digits("11111"))