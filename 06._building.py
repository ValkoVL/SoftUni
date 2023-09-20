floor = int(input())
room = int(input())

for floor_number in range(floor, 0, - 1):
    for room_number in range(0, room):
        if floor_number == floor:
            print(f"L{str(floor_number)}{str(room_number)}", end=" ")
        elif floor_number % 2 == 0:
            print(f'O{str(floor_number)}{str(room_number)}', end=" ")
        else:
            print(f'A{str(floor_number)}{str(room_number)}', end=" ")
    print()

# floors = int(input())
# rooms_of_floors = int(input())

# for floor in reversed(range(1, floors + 1)):
#
#     room_type = 'A' if floor % 2 else 'O'
#     # room_type = 'A' if floor % 2 == 0 else 'O'
#     if floor == floors:
#         room_type = 'L'
#
#     for room in range(rooms_of_floors):
#         room_name = f'{room_type}{floor}{room}'
#         print(room_name, end=" ")

