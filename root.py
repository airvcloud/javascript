import math
import time
print("Program to find root of squares using differential laws:-\n\n")
x = int(input("Enter value of x: "))
dx =int(input("Enter value of dx: "))
add = x + dx
print(f"So you are finding value of √{add }")
sqrt_of_x = (math.sqrt(x))
final_root = sqrt_of_x  + 1 / (2 * sqrt_of_x)* dx
time.sleep(1)
print(f"We Know , f(x + dx)= f(x)+ f'(x)x dx")
print(f" f({x} + {dx}) = f({x})+ f'({x}). {dx}")
print(f" f({add})    = f({x})+ f'({x}). {dx} ")
print(f"(√ {add})  = (√{x})+ (1 / 2  x √{x}). {dx}")
print(f"(√ {add})  = {sqrt_of_x} +  1 / ( 2 *{sqrt_of_x}) .  {dx}")
print(f"(√{add})   = {final_root} ")
