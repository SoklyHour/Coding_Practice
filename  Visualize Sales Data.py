import matplotlib.pyplot as plt

def plot_sales(sales_data):
    sales_summary = {}
    for sale in sales_data:
        product = sale['product']
        sales_summary[product] = sales_summary.get(product, 0) + sale['amount']

    products = list(sales_summary.keys())
    amounts = list(sales_summary.values())

    plt.bar(products, amounts)
    plt.xlabel('Products')
    plt.ylabel('Total Sales')
    plt.title('Total Sales by Product')
    plt.show()

# Example usage
sales_data = [
    {'product': 'A', 'amount': 100},
    {'product': 'B', 'amount': 150},
    {'product': 'A', 'amount': 200},
]
plot_sales(sales_data)
