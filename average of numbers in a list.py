# How do you find the average of numbers in a list?
# To find the average of numbers in a list, sum all the numbers and divide by the count of numbers.

def average_num(numbers):
    if not numbers:
        return 0
    
    return sum(numbers) / len(numbers)  

print(average_num([1, 2, 3, 4, 5]))  # Output: 3.0
print(average_num([10, 20, 30]))      # Output: 20.0
print(average_num([]))                 # Output: 0
print(average_num([-1, 0, 1]))        # Output: 0.0