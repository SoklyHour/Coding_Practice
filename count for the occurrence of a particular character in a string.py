# How do you find the count for the occurrence of a particular character in a string?

# You can traverse the string and tally the instances of the specific character.

def count_character_occurrence(input_string, char):
    count = 0
    
    for c in input_string:
        if c == char:
            count += 1
    return count

print(count_character_occurrence("hello world", "o"))  # Output: 2
print(count_character_occurrence("banana", "a"))       # Output: 3
print(count_character_occurrence("character", "c"))     # Output: 2
print(count_character_occurrence("example", "x"))       # Output: 1