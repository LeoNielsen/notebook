import random

class Student():
    def __init__(self,name,gender,data_sheet,image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self):
        grades = self.data_sheet.get_grades_as_list()
        avg = sum(grades)/len(grades)
        return avg

class DataSheet():
    def __init__(self, *course):
        self.course = course
    
    def get_grades_as_list(self):
        grades = []
        for g in self.course:
            grades.append(g.grade)
        
        return grades

class Course():
    def __init__(self, name, classroom, teacher, ETCS, grade=None):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade
    


###

courses = [Course("Data Science","1.05","Thomas Hartmann",10),Course("Security","1.05","Daniel E.",10),Course("GameDev","1.05","Jesper",10)]
names = ["Anders","Nikolaj","Bent","Ole","Hans","Tim"]
grades = [-3,0,2,4,7,10,12]

def create_students(n):
    students = []

    for x in range(n):
        student = Student(random.choice(names),"male",DataSheet(random.choice(courses),random.choice(courses)),"url")
        students.append(student)
    
    return students

students = create_students(2)

for s in students:
    for i in s.data_sheet.course:
        i.grade = random.choice(grades)
        print(i.name)
        print(i.grade)

    print(s.get_avg_grade())
