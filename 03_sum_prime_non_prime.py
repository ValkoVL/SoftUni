command = input()

prime_sum = 0
non_prime_sum = 0

while command != 'stop':
    curent_number = int(command)

    if curent_number < 0:
        print("Number is negative.")
        command = input()
        continue

    count = 0
    for i in range(1, curent_number + 1):
        if curent_number % i == 0:
            count += 1

    if count == 2:
        prime_sum += curent_number
    else:
        non_prime_sum += curent_number

    command = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
