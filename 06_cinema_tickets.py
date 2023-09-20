input_line = input()

while input_line != "Finish":
    name_of_film = input_line
    available_tickets = int(input())

    current_ticket_count = 0
    command_line = input()
    # Задаваме самостоятелно име в рамките на самостоятелния цикъл!!!
    while command_line != "End":
        type_ticket = command_line
        current_ticket_count += 1

        if current_ticket_count == available_tickets:
            break

        command_line = input()

    percentage_current_movie = current_ticket_count / available_tickets * 100
    print(f"{name_of_film} - {percentage_current_movie:.2f}% full.")

    input_line = input()


# input_line = input()
#
# standard = 0
# student = 0
# kid = 0
#
# while input_line != "Finish":
#     name_of_film = input_line
#     available_billets = int(input())
#
#     while input_line != "End":
#         input_line = input()
#         if input_line == 'student':
#             student += 1
#         elif input_line == 'standard':
#             standard += 1
#         elif input_line == 'kid':
#             kid +=1
#         total_billets = standard + student + kid
#         stand_tickets = standard / total_billets
#         stud_tickets = student / total_billets
#         kid_tickets = kid / total_billets
#
#         if input_line == "End":
#             audientia = total_billets / available_billets * 100
#             print(f"{name_of_film} - {audientia:.2f}% full.")
#
#             break
#             input_line = input()
#         if input_line == "Finish":
#             print(f"{name_of_film} - {audientia:.2f}% full.")
#             print(f'Total tickets: {total_billets}')
#             print(f'{stud_tickets/total_billets} student tickets.')
#             print(f'{stand_tickets/total_billets} standard tickets.')
#             print(f'{kid_tickets / total_billets} kids tickets.')
#             break

# Липсва проверка дали билетите са изчерпани, което води до очакване на нов вход!!!