number_of_cat = int(input())

groop_1 = 0
groop_2 = 0
groop_3 = 0
quantity = 0

for _ in range(number_of_cat):
    quantity_of_food = float(input())
    quantity += quantity_of_food

    if 100 <= quantity_of_food < 200:
        groop_1 += 1

    if 200 <= quantity_of_food < 300:
        groop_2 += 1

    if 300 <= quantity_of_food < 400:
        groop_3 += 1

total_quantity_kg = quantity / 1000
price_of_food = total_quantity_kg * 12.45

print(f'Group 1: {groop_1} cats.')
print(f'Group 2: {groop_2} cats.')
print(f'Group 3: {groop_3} cats.')
print(f'Price for food per day: {price_of_food:.2f} lv.')
