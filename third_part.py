
from functools import reduce

names = ["Ana", "Nino", "Luka", "Giorgi", "Mariam"]
scores = [45, 82, 91, 38, 74]

def pair_students(names_list, scores_list):
    paired_data = list(zip(names_list, scores_list))
    return paired_data

def get_passed_students(paired_data, passing_score=60):
    passed_students = list(filter(lambda student: student[1] >= passing_score, paired_data))
    return passed_students

def calculate_average_of_passed(passed_students):
    scores = list(map(lambda student: student[1], passed_students))

    total = reduce(lambda x, y: x + y, scores)

    average = total / len(scores)

    return average

paired_data = pair_students(names, scores)
passed_students = get_passed_students(paired_data)
average = calculate_average_of_passed(passed_students)

print("Paired students:", paired_data)
print("Passed students:", passed_students)
print("Average score:", average)
