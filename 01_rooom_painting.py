import math

paint_boxes = int(input())
rolls_of_wallpaper = int(input())
gloves_price = float(input())
brush_price = float(input())

paint_price = paint_boxes * 21.5
wallpapers_price = rolls_of_wallpaper * 5.20
number_of_gloves = math.ceil(rolls_of_wallpaper * 35 / 100)
number_of_brushes = math.floor(paint_boxes * 48 / 100)

price_of_products = paint_price + wallpapers_price + (number_of_gloves * gloves_price) + (number_of_brushes * brush_price)
delivery_price = price_of_products / 15

print(f'This delivery will cost {delivery_price:.2f} lv.')