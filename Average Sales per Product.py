def average_sales_per_product(sales_data):
    sales_summary = {}
    for sale in sales_data:
        product = sale['product']
        sales_summary[product] = sales_summary.get(product, {'total': 0, 'count': 0})
        sales_summary[product]['total'] += sale['amount']
        sales_summary[product]['count'] += 1

    return {product: summary['total'] / summary['count'] for product, summary in sales_summary.items()}

# Example usage
sales_data = [
    {'product': 'A', 'amount': 100},
    {'product': 'A', 'amount': 200},
    {'product': 'B', 'amount': 150},
]
print(average_sales_per_product(sales_data))  # Output: {'A': 150.0, 'B': 150.0}
