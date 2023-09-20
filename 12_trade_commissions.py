city = input()
trade_vollume = float(input())

wrong_data = False
commissions = 0

if city == 'Sofia':
    if 0 <= trade_vollume <= 500:
        commissions = trade_vollume * 0.05
    elif 500 <= trade_vollume <= 1000:
        commissions = trade_vollume * 0.07
    elif 1000 <= trade_vollume <= 10000:
        commissions = trade_vollume * 0.08
    elif trade_vollume > 10000:
        commissions = trade_vollume * 0.12
    else:
        print(wrong_data)

if city == 'Varna':
    if 0 <= trade_vollume <= 500:
        commissions = trade_vollume * 0.045
    elif 500 <= trade_vollume <= 1000:
        commissions = trade_vollume * 0.075
    elif 1000 <= trade_vollume <= 10000:
        commissions = trade_vollume * 0.10
    elif trade_vollume > 10000:
        commissions = trade_vollume * 0.13
    else:
        print(wrong_data)

if city == 'Plovdiv':
    if 0 <= trade_vollume <= 500:
        commissions = trade_vollume * 0.055
    elif 500 <= trade_vollume <= 1000:
        commissions = trade_vollume * 0.08
    elif 1000 <= trade_vollume <= 10000:
        commissions = trade_vollume * 0.15
    elif trade_vollume > 10000:
        commissions = trade_vollume * 0.145
    else:
        print(wrong_data)

if wrong_data == True:
    print('error')

else:
   print(f'{commissions:.2f}')




