x1=int(input("Enter rook X coordinates:"))
y1=int(input("Enter rook Y coordinates: "))
x2=int(input("Enter target X coordinates: "))
y2=int(input("Enter target Y coordinates: "))
if x1 > 8 or x2 > 8 or y1 > 8 or y2 > 8 or x1 < 1 or y1 < 1 or x2 < 1 or y2 < 1:
    print("Invalid coordinates!")
elif x1 == x2 and y1 == y2:
    print("The rook and the target have the same coordinates.")
elif x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")