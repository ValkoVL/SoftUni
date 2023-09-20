chicken_menu = int(input())
fish_menu = int(input())
vegitarian_menu = int(input())

#•	Пилешко меню –  10.35 лв.
#•	Меню с риба – 12.40 лв.
#•	Вегетарианско меню  – 8.15 лв.

chicken_price = chicken_menu * 10.35
fish_price = fish_menu * 12.4
vegitarian_price = vegitarian_menu * 8.15
total_price = chicken_price + fish_price + vegitarian_price
dessert = total_price * 0.2

total_cost = total_price + dessert + 2.50

print(total_cost)
