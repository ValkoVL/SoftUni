quantity_food_kg = int(input('Food available (kg): '))
eaten_quantity = 0
command = ""
food_in_gr = quantity_food_kg * 1000
Flag = False

while command != "Adopted":
    command = input('eaten (gr.): ')
    if command != "Adopted":
        eaten_food = command
        eaten_quantity += int(eaten_food)
        diff_rest_food = int(food_in_gr) - int(eaten_quantity)

        if diff_rest_food <= 500 and diff_rest_food > 0:
            print(f'You have only {diff_rest_food} grams of food more')
            # break
    else:
        Flag = True
        break

while command == "Adopted":
    diff = abs(eaten_quantity - food_in_gr)
    if eaten_quantity > food_in_gr:
        print(f"Food is not enough. You need {diff} grams more.")
    elif food_in_gr >= eaten_quantity:
        print(f"Food is enough! Leftovers: {diff} grams.")
    break
