num = int(input())

for current_string in range(num):
    input_line = input()
    if "," in input_line or \
        "." in input_line or \
        "_" in input_line:
        print(f'{input_line} is not pure!')
    else:
        print(f'{input_line} is pure.')
