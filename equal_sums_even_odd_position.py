num1 = input()
num2 = input()

for number in range (int(num1), int(num2) + 1):
    current_num_str = str(number)

    sum_even = 0
    sum_odd = 0

    for num in range(0, len(current_num_str)):
        digit = int(current_num_str[num])
        if num % 2 == 0:
            sum_even += digit
        else:
            sum_odd += digit

    if sum_even == sum_odd:

        print(f'{number}' '', end=' ')
