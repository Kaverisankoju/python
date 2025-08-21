# Total seconds
total_seconds = int(input("Enter total seconds: "))

# Calculate hours
hours = total_seconds // 3600

# Calculate minutes
minutes = (total_seconds % 3600) // 60

# Calculate seconds
seconds = total_seconds % 60

# Print result
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)
