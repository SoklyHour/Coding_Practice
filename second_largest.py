from email.policy import default


def find_second_largest_sorted(numbers):
    """Finds the second largest element using sorting and indexing."""
    
    if len(numbers) < 2:
        return None  # Handle cases with less than 2 elements

    # Sort the list in descending order
    sorted_numbers = sorted(numbers, reverse=True)

    # Return the second element (assuming no duplicates)
    return sorted_numbers[1]

# Example usage
numbers = [5, 8, 2, 9, 1]
second_largest = find_second_largest_sorted(numbers)

print(f"Second largest (sorted): {second_largest}")

def find_second_smallest_sorted(numbers):
    """Finds the second largest element using sorting and indexing."""
    
    if len(numbers) < 2:
        return None  # Handle cases with less than 2 elements

    # Sort the list in descending order
    sorted_numbers = sorted(numbers)

    # Return the second element (assuming no duplicates)
    return sorted_numbers[1]

# Example usage
numbers = [5, 8, 2, 9, 1]
second_smallest = find_second_smallest_sorted(numbers)

print(f"Second smallest (sorted): {second_smallest}")
