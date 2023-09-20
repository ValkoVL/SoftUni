given_string = input()

while given_string != "End":

    if given_string != 'SoftUni':
        new_string = ''
        for char in given_string:
            new_string += char * 2
        print(new_string)

    given_string = input()
