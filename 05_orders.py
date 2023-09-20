orders = int(input())

total_price = 0

for _ in range(0, orders):
    price_per_capsule = float(input())
    days = int(input())
    needed_capsules_per_day = int(input())

    if 0 < price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= needed_capsules_per_day <= 2000:
        current_price = price_per_capsule * needed_capsules_per_day
        order_price = current_price * days
        total_price += order_price
        print(f"The price for the coffee is: ${order_price:.2f}")

    else:
        continue

print(f"Total: ${total_price:.2f}")
