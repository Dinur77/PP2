#Ex1
class Student(Person):

#Ex2
 class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

 class Student(Person):
  pass

x = Student("Mike")
x.printname()

