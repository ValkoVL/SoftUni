# command = input()
#
# Flag = False
# while True:
#
#     while command != "Voldemort":
#         name = command
#         # command = input()
#         if len(name) < 5:
#             print(f"{name} goes to Gryffindor.")
#         if len(name) == 5:
#             print(f"{name} goes to Slytherin.")
#         if len(name) == 6:
#             print(f"{name} goes to Ravenclaw.")
#         if len(name) > 6:
#             print(f"{name} goes to Hufflepuff.")
#         if command == "Voldemort":
#             print("You must not speak of that name!")
#         break
#
#     # if command == "Welcome!":
#     #     Flag = True
#     #     print("Welcome to Hogwarts.")
#     #     break
#
#     command = input()
#
#     if command == "Welcome!":
#         Flag = True
#         print("Welcome to Hogwarts.")
#     break

Flag = False

while not Flag:
    command = input()

    if command == "Welcome!":
        Flag = True
        print("Welcome to Hogwarts.")

    elif command == "Voldemort":
        Flag = True
        print("You must not speak of that name!")
        # break
    else:
        name = command
        if len(name) < 5:
            print(f"{name} goes to Gryffindor.")
        elif len(name) == 5:
            print(f"{name} goes to Slytherin.")
        elif len(name) == 6:
            print(f"{name} goes to Ravenclaw.")
        else:
            print(f"{name} goes to Hufflepuff.")
