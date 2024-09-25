def top_n_products(sales_data, n):
    sales_summary = {}
    for sale in sales_data:
        product = sale['product']
        sales_summary[product] = sales_summary.get(product, 0) + sale['amount']

    return sorted(sales_summary.items(), key=lambda x: x[1], reverse=True)[:n]

# Example usage
sales_data = [
    {'product': 'A', 'amount': 100},
    {'product': 'B', 'amount': 150},
    {'product': 'A', 'amount': 200},
]
print(top_n_products(sales_data, 2))  # Output: [('A', 300), ('B', 150)]
