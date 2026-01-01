from school import School , Classroom , Subject
from persons import Student ,Teacher
def main():
    
    school = School('Adam jee','U TT RA')

    # cls
    eight = Classroom('eight')
    school.add_classroom(eight)
    nine = Classroom('nine')
    school.add_classroom(nine)
    ten = Classroom('ten')
    school.add_classroom(ten)

    # add students
    Abir = Student('Abir khan', eight)
    school.student_admission(Abir)
    kabir = Student('kabir khan', eight)
    school.student_admission(kabir) 
    sabbir = Student('sabbir khan', eight)
    school.student_admission(sabbir)


    #subjects
    physics_teacher = Teacher('MH shanto')
    physics = Subject('Physics', physics_teacher)
    eight.add_subject(physics)

    chemistry_teacher = Teacher('Tushi sorkar')
    chemistry = Subject('chemistry', chemistry_teacher)
    eight.add_subject(chemistry)
    

    math_teacher = Teacher('Fatin Istiak')
    math = Subject('math', math_teacher)
    eight.add_subject(math)

    eight.take_semester_final()
    
    
    
    print(school)
    

if __name__ == '__main__':
     main()