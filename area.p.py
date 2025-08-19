import math  # Import the math module to use math.pi

# Input: radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate perimeter (circumference)
perimeter = 2 * math.pi * radius

# Calculate area
area = math.pi * radius ** 2

# Print results
print("Perimeter (Circumference):", round(perimeter, 2))
print("Area:", round(area, 2))
