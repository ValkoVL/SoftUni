breed = input()
sex = input()

cat_month = 0

if breed == "British Shorthair":
    if sex == "m":
        cat_month = int(13 * 12 / 6)
    elif sex == "f":
        cat_month = int(14 * 12 / 6)
    print(f'{cat_month} cat months')
elif breed == "Siamese":
    if sex == "m":
        cat_month = int(15 * 12 / 6)
    elif sex == "f":
        cat_month = int(16 * 12 / 6)
    print(f'{cat_month} cat months')
elif breed == "Persian":
    if sex == "m":
        cat_month = int(14 * 12 / 6)
    elif sex == "f":
        cat_month = int(15 * 12 / 6)
    print(f'{cat_month} cat months')
elif breed == "Ragdoll":
    if sex == "m":
        cat_month = int(16 * 12 / 6)
    elif sex == "f":
        cat_month = int(17 * 12 / 6)
    print(f'{cat_month} cat months')
elif breed == "American Shorthair":
    if sex == "m":
        cat_month = int(12 * 12 / 6)
    elif sex == "f":
        cat_month = int(13 * 12 / 6)
    print(f'{cat_month} cat months')
elif breed == "Siberian":
    if sex == "m":
        cat_month = int(11 * 12 / 6)
    elif sex == "f":
        cat_month = int(12 * 12 / 6)
    print(f'{cat_month} cat months')

else:
    print(f'{breed} is invalid cat!')
