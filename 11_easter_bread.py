budget = float(input())
price_flour = float(input())

eggs = 0
current_count_of_loaves = 0
used_budget = 0

Flag = False
while True:
    if Flag:
        break
    milk_price = price_flour * 1.25 * 0.25
    egg_price = price_flour * 0.25
    price_of_products_for_one_loaf = price_flour + milk_price + egg_price * 3
    used_budget += price_of_products_for_one_loaf
    current_count_of_loaves += 1
    eggs += 3
    remaining_budget = budget - used_budget
    if current_count_of_loaves % 3 == 0:
        eggs -= current_count_of_loaves - 2
    if remaining_budget < price_of_products_for_one_loaf:
        Flag = True
        print(f'You made {current_count_of_loaves} loaves of Easter bread! Now you have {eggs} eggs and {remaining_budget:.2f}BGN left.')
