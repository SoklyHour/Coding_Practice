def square_list_loop(numbers):
    
  """Squares all elements in a list using a loop."""

  squared_numbers = []

  for number in numbers:

    squared_numbers.append(number * number)

  return squared_numbers


# Example usage

numbers = [1, 2, 3, 4, 5]

squared_numbers = square_list_loop(numbers)

print(f"Squared list (loop): {squared_numbers}")

