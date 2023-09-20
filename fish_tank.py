lenght = int(input())
wight = int(input())
height = int(input())
percent_acc = float(input())

volume = lenght * wight * height
total_lt = volume / 1000
volume_acc = total_lt * (percent_acc / 100)
result = total_lt - volume_acc
print(result)