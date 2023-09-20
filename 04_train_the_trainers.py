number_of_people_on_the_jury = int(input())
# evaluation = float(input())

sum_of_evaluations = 0
counter = 0
count_presentations = 0
average_all_presentations = 0

while True:
    input_line = input()
    name_of_presentation = input_line
    if input_line == 'Finish':
        total_average_evaluation = average_all_presentations / count_presentations
        print(f"Student's final assessment is {total_average_evaluation:.2f}.")
        break

    for _ in range (number_of_people_on_the_jury):
        evaluation = float(input())
        sum_of_evaluations += evaluation
        counter += 1

        if counter == number_of_people_on_the_jury:
            average_evaluation = sum_of_evaluations / number_of_people_on_the_jury
            count_presentations += 1
            average_all_presentations += average_evaluation
            break

    print(f'{name_of_presentation} - {average_evaluation:.2f}.')
    counter = 0
    sum_of_evaluations = 0

    # input_line = input()

    # if input_line == "Finish":
    #     total_average_evaluation = average_all_presentations / count_presentations
    #     print(f"Student's final assessment is {total_average_evaluation:.2f}.")
    #     break

# total_average_evaluation = average_all_presentations / count_presentations
# print(f"Student's final assessment is {total_average_evaluation:.2f}.")

