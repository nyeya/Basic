point1 = eval(input("Enter the x,y cordinate of the first point[Ex: (2,5)]: "))
point2 = eval(input("Enter the x,y cordinate of the second point[Ex: (4,9)]: "))
midpoint_x = (point1[0]+point2[0])/2
midpoint_y = (point1[1]+point2[1])/2
print(f"\nThe midpoint of line from point A{point1} to point B{point2} is ({midpoint_x}, {midpoint_y})")
