class student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id
    
    def __repr__(self):
        return f'Student with name: {self.name }, class: {self.current_class}, id: {self.id}'
    

class Teacher:
    def __init__(self, name, subject , id): 
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self):
        return f'Teacher with name: {self.name}, subject: {self.subject}, id: {self.id}' 

class School:
    def __init__(self,name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            return 'not enough fee'
        else:
            id = len(self.students) + 1
            new_student = student(name, 'c', id)
            self.students.append(new_student)
            return f'{name} is enrolled with id: {id}, extra money {fee - 6500}'

    def __repr__(self):
        print('Welcome to ', self.name)
        print('------our TEachers------')
        for teacher in self.teachers:
            print(teacher)

        print('---our students')
        for student in self.students:
            print(student)
            return ('All done for now')


        



# Mannan = Teacher('Mannan sir', 'Math', 75)
# print(Mannan)
# alia = student('Alia torkare', 7, 22)
# print(alia) 

phitron = School('phitron')
phitron.enroll('alia', 5400)
phitron.enroll('rani', 8900)
phitron.enroll('vaijan',8000)

phitron.add_teacher('Tom cursie', 'DS')
phitron.add_teacher('DECam', 'Dgg')
phitron.add_teacher('aj', 'database')

print(phitron)


 