from math import pi
def area():
    try:
        r = float(input("Enter the radius of a circle: "))
    except(ValueError):
        print ("Invalid Value!")
        return area()
    if r <= 0:
        print ("Invalid Value!")
        return area()
    
    S = pi * r*r
    print(S)
area()