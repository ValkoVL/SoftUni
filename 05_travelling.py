input_line = input()
saved_money = 0

while input_line != 'End':
    destination = input_line
    budget = float(input())

    while saved_money < budget:
        won_money = float(input())
        saved_money += won_money

        if saved_money >= budget:
            flag = True
            print(f"Going to {destination}!")
            saved_money = 0
            break

    input_line = input()
