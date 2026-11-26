# Program to calculate area and perimeter of a rectangle
length_in_cm = float(input("Enter the length in cm: "))
breadth_in_cm = float(input("Enter the breadth in cm: "))
# Calculate area and perimeter
area_in_square_cm = length_in_cm * breadth_in_cm
perimeter_in_cm = 2 * (length_in_cm + breadth_in_cm)
# Display the results
print("Area of the rectangle =", area_in_square_cm, "square cm")
print("Perimeter of the rectangle =", perimeter_in_cm, "cm")