number_procesors = int(input())
number_staff = int(input())
workdays = int(input())

total_hours = number_staff * workdays * 8
productivity = int(total_hours / 3)
diff = abs(number_procesors - productivity)

if productivity > number_procesors or productivity == number_procesors:
    profit = diff * 110.1
    print(f'Profit: -> {profit:.2f} BGN')
else:
    profit = diff * 110.1
    print(f'Losses: -> {profit:.2f} BGN')
