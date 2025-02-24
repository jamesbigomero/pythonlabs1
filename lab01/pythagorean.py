import math
side1 = input("Enter the first side of the triangle: ")
side2 = input("Enter the second side of the triangle: ")

print(f"You entered side1: {side1} and side2: {side2}")
side1 = float(side1)
side2 = float(side2)
  
hypotenuse = math.sqrt(side1 ** 2 + side2 ** 2)
    
print(f"The hypotenuse is {hypotenuse:.2f}")