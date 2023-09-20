num = int(input())
left_sum = 0
right_sum = 0

for _ in range(num):
    current_sum = int(input())
    left_sum += current_sum

for _ in range(num):
    current_sum = int(input())
    right_sum += current_sum

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')

else:
    diff = abs(left_sum - right_sum)
    print(f'No, diff = {diff}')
