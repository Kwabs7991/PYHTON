#Object Oriented Programming in Pyhton:

class Student:

  def __init__(self, name, age, year_grade):
    self.age = age
    self.name = name
    self.year_grade = year_grade  # 0 - 100

#Setting Functions, Setters
  def set_age(self, age):
    self.age = age
  
  def set_name(self, name):
    self.name = name

  def set_year_grade(self, year_grade):
    self.year_grade = year_grade


#Getting Functions, Getters
  def get_age(self):
    return self.age

  def get_name(self):
    return self.name

  def get_year_grade(self):
    return self.year_grade

  


class Course:
  def __init__(self, name, max_students):
    self.name = name
    self.max_students = max_students
    self.students = []

  def add_student(self, student):
    if len(self.students) < self.max_students:
      self.students.append(student)
      return True
    return False

  def get_average_grade(self):
    value  = 0
    for Student in self.students:
      value += Student.get_year_grade()

    return value / len(self.students)

s1 = Student("Timonthy", 19, 83)
s2 = Student("Samantha", 19, 99)
s3 = Student("Simon", 19, 63)
s4 = Student("Damien", 19, 80)
s5 = Student("Raquel", 19, 77)

course_science = Course("Science", 2)
course_science.add_student(s1)
course_science.add_student(s2)


print(course_science.students[0].age)
print(course_science.students[0].name)
print(course_science.students[0].year_grade)
print("\n")
print(course_science.students[1].age)
print(course_science.students[1].name)
print(course_science.students[1].year_grade)
print("\n")
print(course_science.get_average_grade())
