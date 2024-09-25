# Write a Python program to find the largest element in a list.
def find_largest(numbers):
    largest =numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
    return largest

nums = [10, 20, 1]
largest_numbers = find_largest(nums)

print(f"The largest number is {largest_numbers}")

# Write a Python program to find the smallest element in a list.

def find_smallest(numbers):
    smallest = numbers[0]

    for num in numbers:
        if num < smallest:
            num = smallest
    return smallest
    
num = [1,2,3,4]
smallest_numbers = find_smallest(num)
print(f"{smallest_numbers}")