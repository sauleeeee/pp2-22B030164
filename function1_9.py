import math
def volume(rad):
    return (4/3)*math.pi* ( rad * rad * rad)
rad = float(input("Enter the radius of the circle: "))
print("The volume of the circle:",volume(rad))
