first_string = input()
second_string = input()

transformed_string = first_string
# using slice
for letter in range(len(first_string)) :
    first_part = second_string[:letter + 1]
    second_part = first_string[letter + 1:]
    new_string = first_part + second_part

    if new_string != transformed_string:
        print(new_string)
        transformed_string = new_string
