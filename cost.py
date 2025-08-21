# Assign price and quantity for Product 1
price1 = 100
quantity1 = 2

# Assign price and quantity for Product 2
price2 = 150
quantity2 = 3

# Calculate cost for each product
cost1 = price1 * quantity1
cost2 = price2 * quantity2

# Calculate total before tax
total_before_tax = cost1 + cost2

# Calculate tax (18%)
tax = total_before_tax * 0.18

# Calculate total cost after tax
total_after_tax = total_before_tax + tax

# Print detailed bill
print("----- BILL -----")
print("Product 1: ₹", price1, "x", quantity1, "= ₹", cost1)
print("Product 2: ₹", price2, "x", quantity2, "= ₹", cost2)
print("Subtotal      = ₹", total_before_tax)
print("Tax (18%)     = ₹", round(tax, 2))
print("Total Amount  = ₹", round(total_after_tax, 2))
