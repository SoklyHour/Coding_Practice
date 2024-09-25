
fruits = {"apple": 2, "banana": 3, "cherry": 1}

total_quantity = 0

for fruit, quantity in fruits.items():

  print(f"{fruit}: {quantity}")

  total_quantity += quantity

print(f"Total quantity: {total_quantity}")

