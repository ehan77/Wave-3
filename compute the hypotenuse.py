# IMPORTS
from math import sqrt
import time
# INPUTS
legA = int(input("Enter the length of leg A: "))
legB = int(input("Enter the length of leg B: "))

print("Calculating the hypotenuse...")
time.sleep(3)

hyp = round(sqrt(legA * legA + legB *legB), 2)

print("The hypotenuse is" , hyp , ", leg A is" , legA , "and leg B is" , legB , ".")