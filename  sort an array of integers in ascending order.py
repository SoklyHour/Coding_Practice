# How do you sort an array of integers in ascending order?
# You can employ sorting methods like bubble sort, selection sort, or the innate sorting features in programming languages.

def sort_array_ascending(arr):
    arr.sort()

arr = [5, 3, 8, 1, 2, 11]
sort_array_ascending(arr)  # Sorts the array in place
print(arr)  # Output: [1, 2, 3, 5, 8, 11]