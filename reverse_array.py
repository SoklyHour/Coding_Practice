# How do you reverse an array?
# Reversing an array can be done by swapping elements from the start and end until you reach the middle of the array.

def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]  # Use assignment, not comparison
        left += 1
        right -= 1

    return arr  

arr = [1, 2, 3, 4, 5]
reverse_array(arr)

print(arr)  # Output: [5, 4, 3, 2, 1]