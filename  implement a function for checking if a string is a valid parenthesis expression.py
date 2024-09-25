def is_valid_parenthesis(expression):
    """Checks if a string is a valid parenthesis expression."""
    stack = []
    mapping = {"(": ")", "{": "}", "[": "]"}

    for char in expression:
        if char in mapping:  # If the character is an opening bracket
            stack.append(char)
        elif char in mapping.values():  # If the character is a closing bracket
            if not stack or mapping[stack.pop()] != char:  # Check for a match
                return False

    return not stack  # Return True if stack is empty (all brackets matched)

# Example usage
expression = "([)]"

if is_valid_parenthesis(expression):
    print(f"{expression} is a valid parenthesis expression.")
else:
    print(f"{expression} is not a valid parenthesis expression.")
print(is_valid_parenthesis("()"))         # True
print(is_valid_parenthesis("([])"))       # True
print(is_valid_parenthesis("{[()]}"))     # True
print(is_valid_parenthesis("((()))"))     # True
print(is_valid_parenthesis("((()"))       # False
print(is_valid_parenthesis("{[)]}"))      # False