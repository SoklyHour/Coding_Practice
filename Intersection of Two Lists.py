def intersection(list1, list2):
    return list(set(list1) & set(list2))

# Example usage
print(intersection([1, 2, 3], [2, 3, 4]))  # Output: [2, 3]
