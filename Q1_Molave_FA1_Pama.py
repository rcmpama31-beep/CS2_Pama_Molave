import math
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt(math.pow((x2 - x1),2) + math.pow((y2 -y1), 2))
print (distance)

# Reflection
# Using math library is much easier than writing every step from scratch because it save more time and prevent mistakes.
# Functions like sqrt and pow quickly handle hard calculations, like finding square roots, using just one line of code.
# Without them, solving geometry formulas would require writing long and complicated steps by hand.