input_line = input()

coffee_counter = 0

while input_line != "END":

    # lower() приравнява израза на малки букви, а upper - на големи букви. Избягва се двояна проверка.
    if input_line.lower() == "coding" or \
            input_line.lower() == "dog" or \
            input_line.lower() == "cat" or \
            input_line.lower() == "movie":
        # islower() - ПРОВЕРЯВА дали изръзът е с малки букви!!!
        if input_line.islower():
            coffee_counter += 1
        else:
            coffee_counter += 2

    input_line = input()
if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)
