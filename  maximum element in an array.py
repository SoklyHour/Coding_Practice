# How do you find the maximum element in an array?
# To discover the array’s highest value, scan through it and remember the greatest encountered.

def find_max_element(arr):
    if not arr:
        return None
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element

arr = [1, 3, 2, 8, 5]
print(find_max_element(arr))  # Output: 8

empty_arr = []
print(find_max_element(empty_arr))  # Output: None