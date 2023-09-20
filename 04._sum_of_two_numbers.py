first_num = int(input())
end_num = int(input())
magic_num = int(input())

combinations = 0
break_condition = False
right_combination = 0
for number1 in range(first_num, end_num + 1):
    for number2 in range(first_num, end_num + 1):
        combinations += 1

        if number1 + number2 == magic_num:
            # right_combination += 1
            print(f"Combination N:{combinations} ({number1} + {number2} = {magic_num})")
            break_condition = True
            # break

    if break_condition:
        break
        # print(f'Combinations are: {right_combination}')
else:
    print(f"{combinations} combinations - neither equals {magic_num}")
