class Student:
  def_init_(self,name,roll number,cgpa):
    self.name= Name
    self.roll number= roll number  
    self.cgpa=cgpa
def sort_students(students_list):
  sorted_students= sorted(students_list,key=lambda,students:student.cgpa,reverse=true)
  return sorted_students
students = [
  Student("Varsha","A123",7.8),
  Student("Saran","A124",8.9),
  Student("Salim","A125",9.1),
]
sorted_students=sort_students(students)
for student in sorted_students:
  print("Namew: {}, Roll Number {},CGPA: {}".format(student.name,student.roll_number,student.cgpa))