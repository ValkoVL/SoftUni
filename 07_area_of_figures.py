figure = str(input())
area = 0

if figure == 'square':
    a = float(input())
    area = a*a
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a*b
elif figure == 'circle':
    r = float(input())
    pi = 3.14159265359
    area = pi*r**2
elif figure == 'triangle':
    a = float(input())
    b = float(input())
    area = a * b / 2

print(f"{area:.3f}")