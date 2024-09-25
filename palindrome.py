# How can you check whether a string is a palindrome or not?
# A palindrome is a word or phrase that reads the same both ways, forward and backward. 
# You can simply compare it to its reverse to determine if a string is a palindrome.

def is_palindrome(input_string):
    return input_string==input_string[::-1]
print(is_palindrome("level"))      # True 
print(is_palindrome("hello"))    # Output: False
print(is_palindrome("lol"))  # True 
