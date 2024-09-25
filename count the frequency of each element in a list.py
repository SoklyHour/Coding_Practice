# Write a Python program to count the frequency of each element in a list.

def count_frequency(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:    
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency

test = [1,1,1,2,3,4]
print(count_frequency(test))
