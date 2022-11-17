import random
from unittest import result

class Student():
    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def __repr__(self):
        return "Student(%r,%r,%r,%r)" % (self.name,self.gender,self.data_sheet,self.image_url)

    def get_avg_grade(self):
        return sum(self.data_sheet.get_grades_as_list()) / len(self.data_sheet.get_grades_as_list())

class DataSheet():
    def __init__(self, *courses):
        self.courses = set(courses)

    def __repr__(self):
        return "DataSheet(%r)" % (self.courses)


    def get_grades_as_list(self):
        return list(self.courses.grade)

class Course():
    def __init__(self, name, classroom, teacher, ETCS, grade = None):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade

    def __repr__(self):
        return "Course(%r,%r,%r,%r,%r)" % (self.name,self.classroom, self.teacher,self.ETCS,self.grade)




def generate_students(n):
    courses = [Course("Data Science","1.05","Thomas Hartmann",10),Course("Security","1.05","Daniel E.",10),Course("GameDev","1.05","Jesper",10)]
    f_names = ["Anders","Nikolaj","Bent","Ole","Hans","Tim"]
    l_names = ["Nielsen", "Thomsen","Jensen","Miller","Normann"]
    grades = [-3,0,2,4,7,10,12]
    
    students = []
    
    for i in range(n):   
        student = Student(random.choice(f_names)+ " " +random.choice(l_names),"male",DataSheet(random.choice(courses),random.choice(courses)),"www.image.com/stundent/" + str(i))
        for x in student.data_sheet.courses:
            x.grade = random.choice(grades)
        students.append(student)
    
    with open("result.csv","w") as f:
        f.write("stud_name, course_name, teacher, gender, ects, classroom, grade, img_url\n")
        for j in students:
            for k in student.data_sheet.courses:
                f.write(str("%r,%r,%r,%r,%r,%r,%r,%r \n"%(j.name,k.name,k.teacher,j.gender,k.ETCS,k.classroom,k.grade,j.image_url)))


generate_students(10)

with open("result.csv") as f:
    lines = f.readlines()
    del lines[0]
    for i in lines:
        i = i.split(",")