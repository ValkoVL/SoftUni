nylon = float(input())
paint = float (input())
thinner = int(input())
work_hours = float (input())

nylon_price = (nylon + 2) * 1.50
paint_price = (paint * 1.1) * 14.50
thinner_price = thinner * 5
material_price = nylon_price + paint_price + thinner_price + 0.40

painters_hour = material_price * 0.3

total_price = material_price + (painters_hour * work_hours)

print(total_price)