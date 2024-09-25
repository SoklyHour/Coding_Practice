# How do you calculate the number of vowels and consonants in a string?
# You can iterate through the string and count the vowels and consonants.

def count_vowels_and_consonants(input_string):
    vowels ="aeiou"
    num_vowels = 0
    num_consonants = 0
    for char in input_string:
        if char.lower() in vowels:
            num_vowels += 1
        else:
            num_consonants += 1

    return num_vowels, num_consonants
print(count_vowels_and_consonants("Hello World!"))  # Output: (3, 7)
print(count_vowels_and_consonants("Python 3.9"))    # Output: (1, 9)
print(count_vowels_and_consonants("abc123"))         # Output: (1, 5)
print(count_vowels_and_consonants("123456"))         # Output: (0, 6)