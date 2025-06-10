a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
largest = max(a, b, c)
sum_two = a + b + c - largest
if sum_two > largest:
    print(f"{a}, {b}, {c} can form a valid triangle!")
else:
    print(f"{a}, {b}, {c} cannot form a valid triangle!")
