import math as m
import numpy as np
from scipy.integrate import quad

# Define the function
def f(x):
    return x**2  # Example: area under y = x^2

# Calculate the area under the curve between limits a and b
a = 20 # lower limit
b = 90  # upper limit

area, error = quad(f, a, b)

print("Area under the curve:", area)



x = 100

y = m.floor(m.sqrt(x))
print(y)

rADIUS = 10

e= (m.degrees(rADIUS))
print(e)

