w = float(input())
h = float(input())

if w / (h * h) > 25:
    print("Overweight")
elif w / (h * h) > 18.5:
    print("Normal weight")
else:
    print("Underweight")