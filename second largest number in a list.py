def second_largest(numbers):
    # Remove duplicates by converting the list to a set, then back to a list
    unique_numbers = list(set(numbers))
    
    # If there are less than 2 unique numbers, return None
    if len(unique_numbers) < 2:
        return None
    
    # Sort the unique numbers in descending order
    unique_numbers.sort(reverse=True)
    # Return the second element (second largest number)
    return unique_numbers[1]

# Example usage
numbers = [12, 35, 1, 10, 34, 1]
result = second_largest(numbers)

if result is None:
    print("There is no second largest number.")
else:
    print(f"The second largest number is: {result}")
