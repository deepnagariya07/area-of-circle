from math import pi

def circlearea():
    r = float(input("what is the radius of the circle"))
    Area =  pi * r **2 
    print("Area of the circle of " + str(r) + " is:" + str(pi* r*r))

circlearea()    

print("Now we will find volume of the sphere")

def volSphere():
    d = float(input("What is the diameter of the sphere"))
    r = float(d/2)
    print(r)
    vol = pi * (4/3) / r**3
    print("Volume of the sphere is : " + str(vol))

volSphere()
