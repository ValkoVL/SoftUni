dep=float(input())
period=int(input())
interest=float(input())

year_interest=dep*float(interest)/100
month_int=year_interest/12

result=month_int*period+dep

print(result)