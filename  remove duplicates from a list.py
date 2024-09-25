def remove_duplicates(numbers):
    # Initialize an empty list to store unique numbers
    unique_numbers = []
    
    # Loop through each number in the input list
    for num in numbers:
        # If the current number is not already in the unique_numbers list
        if num not in unique_numbers:
            # Add the number to the unique_numbers list
            unique_numbers.append(num)
    
    # Return the list containing only unique numbers
    return unique_numbers

# Test the function with a list that contains duplicate numbers
nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]

# Call the remove_duplicates function and store the result
unique_nums = remove_duplicates(nums)

# Print the list of unique numbers
print(unique_nums)
