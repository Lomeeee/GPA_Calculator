#GPA_calculator py code made by LOME

def gpa_calculation(grades):
    grade_points = {"A": 5.0 , "B": 4.0, "C": 3.0, "D": 2.0, "E":1.0, "F": 0.0}
    total_credit_units = 0
    total_grade_points = 0

    for course, credit_units, grade in grades:
        total_credit_units += credit_units
        total_grade_points += grade_points.get(grade, 0.0) * credit_units
    
    if total_credit_units == 0:
        return 0.0
    else:
        return total_grade_points / total_credit_units

    

def main():
    num_courses = int(input("Enter the number of courses: "))
    grades_list=[]
    
    for i in range(num_courses):
        course = input("Enter the name of course {}: ".format(i+1))
        credit_units = float(input("Enter credit unit for {}: ".format(course)))
        grade = (input("Enter grade for {}: ".format(course)))

        grades_list.append((course, credit_units, grade.upper()))

    gpa = gpa_calculation(grades_list)
    print("your GPA is {:.2f}" .format(gpa))

   
if __name__ == "__main__":
    main()
