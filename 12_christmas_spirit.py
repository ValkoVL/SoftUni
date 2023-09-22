quantity_of_decorations_each_time = int(input())
days_left = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
total_cost = 0
total_spirit = 0

for current_day in range(1, days_left + 1):
    if current_day % 11 == 0:
        quantity_of_decorations_each_time += 2
    if current_day % 2 == 0:
        total_cost += quantity_of_decorations_each_time * ornament_set_price
        total_spirit += 5
    if current_day % 3 == 0:
        total_cost += quantity_of_decorations_each_time * tree_skirt_price
        total_cost += quantity_of_decorations_each_time * tree_garland_price
        total_spirit += 3 + 10
    if current_day % 5 == 0:
        total_cost += quantity_of_decorations_each_time * tree_lights_price
        total_spirit += 17
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt_price + tree_garland_price + tree_lights_price

if days_left % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")



# quantity_of_decorations_each_time = int(input())
# days_left = int(input())
#
# ornament_set = 0
# tree_skirt = 0
# tree_garland = 0
# tree_lights = 0
# current_quantity = 0
# total_cost = 0
# total_spirit = 0
#
# for current_day in range(1, days_left + 1):
#     if current_day % 2 == 0:
#         ornament_set += quantity_of_decorations_each_time
#         total_cost += quantity_of_decorations_each_time * 2
#         total_spirit += 5
#
#     if current_day % 3 == 0:
#         tree_skirt += quantity_of_decorations_each_time
#         tree_garland += quantity_of_decorations_each_time
#         total_cost += quantity_of_decorations_each_time * 8
#         total_spirit += 13
#
#     if current_day % 5 == 0:
#         tree_lights += quantity_of_decorations_each_time
#         total_cost += quantity_of_decorations_each_time * 15
#         total_spirit += 17
#
#     if current_day % 10 == 0:
#         tree_skirt += 1
#         tree_garland += 1
#         tree_lights += 1
#         total_cost += 23
#         total_spirit -= 20
#
#         improved_quantity = quantity_of_decorations_each_time + 2
#
#     if current_day % 3 == 0 and current_day % 5 == 0:
#         total_spirit += 30
#
#     if current_day >= 11:
#         improved_quantity = quantity_of_decorations_each_time + 2
#         if current_day % 2 == 0:
#             ornament_set += improved_quantity
#             total_cost += improved_quantity * 2
#             total_spirit += 5
#         if current_day % 3 == 0:
#             tree_skirt += improved_quantity
#             tree_garland += improved_quantity
#             total_cost += improved_quantity * 8
#             total_spirit += 43
#         if current_day % 5 == 0:
#             tree_lights += improved_quantity
#             total_cost += improved_quantity * 15
#             total_spirit += 17
#
#     if current_day == 10:
#         total_spirit -= 30
#
# print(f"Total cost: {total_cost}")
# print(f"Total spirit: {total_spirit}")

