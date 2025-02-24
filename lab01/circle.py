import math
try:
    radius = float(input("Enter the radius of the circle: "))

    
    area = math.pi * (radius ** 2)
    perimeter = 2 * math.pi * radius
    
    print(f"The circle with radius {radius} has an area of {area:.2f} and a perimeter of {perimeter:.2f}.")
    
except ValueError:
    print("Invalid input! Please enter a valid number.")