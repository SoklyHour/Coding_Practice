# mean_tuple function you've defined calculates the mean (average) of each element across multiple tuples (or lists) of numbers
def mean_tuple(numbers):
    result = [sum(x) / len(x) for x in zip(*numbers)]
    return result

# Example input: list of tuples
data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

# Calculate means
means = mean_tuple(data)

# Print the result
print(f"Mean of each position: {means}")
