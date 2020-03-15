'''Learning of class in python'''
'''for creating class we have to write class keyword then name of class'''
class Student:
    '''This is class variable'''
    college = 'Guru Nanak college'
    per_rise =1.05

    def __init__(self,first,last,marks):
        self.first = first # Creating instances of each variable
        self.last = last
        self.marks = marks
        self.email = first + '.' + last +'@school.com'

    def fullname(self): # This function will return full name of object
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):# This will apply percentage increament in marks
        self.marks =int(self.marks*1.05)

class Dumb(Student):
    per_rise = 1.10

    def __init__(self,first,last,marks,prog_lang):
        super().__init__(first,last,marks)
        self.prog_lang = prog_lang

std_1 = Dumb('Prashant','Yadav', 90,'Python')
std_2 = Dumb('Ankur','Yadav',85,'Java')

print(std_1.first)
print(std_1.last)

print(std_1.email)
print(std_2.email)
print(std_1.prog_lang)
print(std_2.prog_lang)
