pa=str(input("do you want to find the perimeter or area of a circle(p for perimeter and a for area)"))
if pa=="a":
    r=float(input("enter the radius of the circle"))
    print("the area is", 3.14159*r**2)
elif pa=="p":
    r=float(input("enter the radius of the circle"))
    print("the perimeter is", 3.14159*2*r)
else:
    print("that is not a valid answer")