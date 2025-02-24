conversions = {
    "cm": (0.393701, "in"), "in": (2.54, "cm"),
    "yd": (0.9144, "m"), "m": (1.09361, "yd"),
    "oz": (28.3495, "g"), "g": (0.035274, "oz"),
    "lb": (0.453592, "kg"), "kg": (2.20462, "lb")
}

user_input = input("Enter value and unit (e.g., '10 cm'): ")
try:
    value, unit = user_input.split()
    value = float(value)
    if unit in conversions:
        factor, new_unit = conversions[unit]
        print(f"{value * factor:.2f} {new_unit}")
    else:
        print("Invalid unit")
except:
    print("Invalid input") 
