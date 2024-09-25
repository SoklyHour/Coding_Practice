def total_sales(sales_data):
    return sum(sale['amount'] for sale in sales_data)

# Example usage
sales_data = [
    {'product': 'A', 'amount': 100},
    {'product': 'B', 'amount': 150},
    {'product': 'C', 'amount': 200},
]
print(total_sales(sales_data))  # Output: 450
