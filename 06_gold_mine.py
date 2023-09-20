number_of_locations = int(input())

for _ in range(number_of_locations):
    exp_yield_per_day = float(input())
    number_of_days = int(input())
    expected_extraction = exp_yield_per_day * number_of_days
    total_extraction = 0

    for _ in range(number_of_days):
        yield_per_day = float(input())
        total_extraction += yield_per_day
        averige_extraction = total_extraction / number_of_days

        diff = abs(averige_extraction - exp_yield_per_day)

    if averige_extraction >= exp_yield_per_day:
        print(f'Good job! Average gold per day: {averige_extraction:.2f}.')

    else:
        print(f'You need {diff:.2f} gold.')
