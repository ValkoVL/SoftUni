num = int(input())
odd_sum = 0
even_sum = 0

for i in range(num):
    current_number = int(input())
    if i % 2 == 0:
        odd_sum += current_number
    else:
        even_sum += current_number

if odd_sum == even_sum:
    print('Yes')
    print(f'Sum = {odd_sum}')
else:
    diff = abs(odd_sum - even_sum)
    print('No')
    print(f'Diff = {diff}')
