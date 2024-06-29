def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

def calculate_average(marks_list):
    total_marks = sum(marks_list)
    average_marks = total_marks / len(marks_list)
    return average_marks

marks_list = [85, 92, 78, 90, 88]
average_marks = calculate_average(marks_list)
grade = calculate_grade(average_marks)

print("Average marks:", average_marks)
print("Grade:", grade)
