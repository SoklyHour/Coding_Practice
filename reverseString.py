# How do you reverse a string?

# Reversing a string is a common coding task. A
# achieve this by looping through the string’s characters and constructing a reversed string.

def reverse_string(input_string):
    return input_string[::-1]
result = reverse_string("hello")
print(result)  # Output: "olleh"
