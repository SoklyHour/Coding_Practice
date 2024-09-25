def segment_customers(customers):
    segments = {}
    for customer in customers:
        total_purchase = customer['total_purchase']
        if total_purchase < 100:
            segment = 'Low'
        elif total_purchase < 500:
            segment = 'Medium'
        else:
            segment = 'High'
        segments[customer['name']] = segment
    return segments

# Example usage
customers = [
    {'name': 'Alice', 'total_purchase': 50},
    {'name': 'Bob', 'total_purchase': 150},
    {'name': 'Charlie', 'total_purchase': 600},
]
print(segment_customers(customers))  # Output: {'Alice': 'Low', 'Bob': 'Medium', 'Charlie': 'High'}
