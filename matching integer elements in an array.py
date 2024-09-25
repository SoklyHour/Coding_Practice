# How do you total all of the matching integer elements in an array?

# Iterate through the array, adding up matching integer elements to find their sum.

def sum_matching_element(arr, target):
    total = 0
    for num in arr:
        if num == target:
            total += num
    return total
print(sum_matching_element([1, 2, 3, 2, 4, 2, 4], 4))  # Output: 8
# This outputs 4 because 4 appears 2 times 
