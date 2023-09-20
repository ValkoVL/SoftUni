# 1.	Първи ред – брой на хората. Цяло число в интервала [1…100]
# 2.	Втори ред – такса вход. Реално число в интервала [0.00…50.00]
# 3.	Трети ред – цена един за шезлонг. Реално число в интервала [0.00…50.00]
# 4.	Четвърти ред – цена за един чадър. Реално число в интервала [0.00...50.00]

import math

people = int(input())
tax = float(input())
cheslong_price = float(input())
umbrella_price = float(input())

tax_people = people*tax

people_cheslong = people * 0.75
ches_price = math.ceil(people_cheslong) * cheslong_price

print(type(ches_price))

people_umbrella = people / 2
umbrella_price = math.ceil(people_umbrella) * umbrella_price

price = tax_people + ches_price + umbrella_price
print(f"{price:.2f}")

